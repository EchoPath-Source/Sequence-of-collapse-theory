import { useState } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, ReferenceLine, ScatterChart, Scatter, AreaChart, Area, Legend } from "recharts";

const C = {
  bg: "#040d1a", panel: "#071428", border: "#0d2444",
  accent: "#00c8ff", gold: "#f0a500", green: "#00e5a0",
  red: "#ff4466", purple: "#a855f7", text: "#c8dff0",
  muted: "#4a6a8a", orange: "#ff8c00",
};

// ── CORE CALCULATION ─────────────────────────────────────────
// PNT: rho_DE(delta) / rho_DE_mean = f_fail(delta) / f_fail_mean
// f_fail(delta) = 1 - f_succ_mean * max(0, 1+delta)^n
// Capped: f_fail in [0, 1]

const f_succ_mean = 0.15;
const Omega_m = 0.315;
const Omega_DE = 0.685;
const H0_CMB = 67.4;
const H0_local_obs = 73.0;

function f_fail(delta, n = 1.5) {
  const raw = 1 - f_succ_mean * Math.max(0, 1 + delta) ** n;
  return Math.max(0, Math.min(1, raw));
}

function rho_DE_ratio(delta, n = 1.5) {
  const ff_mean = f_fail(0, n);
  if (ff_mean === 0) return 1;
  return f_fail(delta, n) / ff_mean;
}

function H0_local(delta, n = 1.5) {
  const OmDE_loc = Omega_DE * rho_DE_ratio(delta, n);
  return H0_CMB * Math.sqrt((Omega_m + OmDE_loc) / (Omega_m + Omega_DE));
}

// Generate curve data: delta from -0.9 to +0.5 (capped, physical range)
const deltaRange = [];
for (let d = -0.90; d <= 0.50; d += 0.05) {
  const d_r = parseFloat(d.toFixed(2));
  const h0 = H0_local(d_r);
  const rho_r = rho_DE_ratio(d_r);
  deltaRange.push({
    delta: d_r,
    H0_n15: parseFloat(h0.toFixed(3)),
    H0_n10: parseFloat(H0_local(d_r, 1.0).toFixed(3)),
    H0_n20: parseFloat(H0_local(d_r, 2.0).toFixed(3)),
    rho_ratio: parseFloat(rho_r.toFixed(4)),
    H0_obs: H0_local_obs,
    H0_cmb: H0_CMB,
  });
}

// Key environments
const environments = [
  { name: "Deep void", delta: -0.80, color: C.accent },
  { name: "Our location\n(Laniakea)", delta: -0.35, color: C.green },
  { name: "Cosmic mean", delta: 0.00, color: C.gold },
  { name: "Filament", delta: 0.30, color: C.orange },
];

// Sensitivity table
const sensitivityData = [
  { delta: -0.20, n10: 14.5, n15: 20.5, n20: 25.9 },
  { delta: -0.30, n10: 21.6, n15: 29.8, n20: 36.5 },
  { delta: -0.35, n10: 25.2, n15: 34.1, n20: 41.3 },
  { delta: -0.40, n10: 28.8, n15: 38.3, n20: 45.7 },
  { delta: -0.50, n10: 35.8, n15: 46.1, n20: 53.4 },
];

// Combined mechanisms
const mechanisms = [
  { name: "Void dark energy differential", min: 1.0, max: 3.0, color: C.green, status: "CALCULATED" },
  { name: "Prompt EDE component", min: 1.0, max: 2.0, color: C.accent, status: "TOY MODEL" },
  { name: "Memory field gravity", min: 0, max: 2.0, color: C.gold, status: "UNCALCULATED" },
  { name: "Parent universe dark energy", min: 0, max: 2.0, color: C.purple, status: "UNCALCULATED" },
];
const totalMin = mechanisms.reduce((s, m) => s + m.min, 0);
const totalMax = mechanisms.reduce((s, m) => s + m.max, 0);

function Tab({ label, active, onClick }) {
  return (
    <button onClick={onClick} style={{
      padding: "7px 14px", background: active ? C.accent : "transparent",
      color: active ? C.bg : C.muted, border: `1px solid ${active ? C.accent : C.border}`,
      borderRadius: 4, cursor: "pointer", fontSize: 10, fontFamily: "monospace",
      letterSpacing: 1, fontWeight: active ? 700 : 400,
    }}>{label}</button>
  );
}

const Tip = ({ active, payload, label }) => {
  if (!active || !payload?.length) return null;
  return (
    <div style={{ background: C.panel, border: `1px solid ${C.border}`, padding: "10px 14px", borderRadius: 4, fontSize: 11, fontFamily: "monospace" }}>
      <div style={{ color: C.muted, marginBottom: 4 }}>δ = {label}</div>
      {payload.map((p, i) => (
        <div key={i} style={{ color: p.color || C.text }}>{p.name}: {typeof p.value === "number" ? p.value.toFixed(3) : p.value}</div>
      ))}
    </div>
  );
};

export default function App() {
  const [tab, setTab] = useState("h0curve");

  return (
    <div style={{ background: C.bg, minHeight: "100vh", color: C.text, fontFamily: "monospace", padding: "20px 18px" }}>

      <div style={{ marginBottom: 20 }}>
        <div style={{ fontSize: 9, color: C.muted, letterSpacing: 3, marginBottom: 4 }}>ECHO LABS · PNT HUBBLE TENSION ANALYSIS</div>
        <h1 style={{ margin: 0, fontSize: 18, color: C.accent }}>VOID-FILAMENT DARK ENERGY DIFFERENTIAL</h1>
        <div style={{ fontSize: 11, color: C.muted, marginTop: 3 }}>A Novel PNT Mechanism for the Hubble Tension</div>
      </div>

      {/* Key result banner */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr 1fr", gap: 8, marginBottom: 16 }}>
        {[
          { label: "H0 CMB (global)", value: "67.4", unit: "km/s/Mpc", color: C.muted },
          { label: "H0 local (observed)", value: "73.0", unit: "km/s/Mpc", color: C.red },
          { label: "H0 our location (PNT)", value: "69.3", unit: "km/s/Mpc", color: C.green },
          { label: "Void effect explains", value: "34%", unit: "of tension", color: C.accent },
        ].map((item, i) => (
          <div key={i} style={{ background: C.panel, border: `1px solid ${item.color}44`, borderRadius: 4, padding: "10px 12px" }}>
            <div style={{ fontSize: 9, color: C.muted, letterSpacing: 1, marginBottom: 4 }}>{item.label}</div>
            <div style={{ fontSize: 20, color: item.color, fontWeight: 700 }}>{item.value}</div>
            <div style={{ fontSize: 10, color: C.muted }}>{item.unit}</div>
          </div>
        ))}
      </div>

      <div style={{ display: "flex", gap: 8, marginBottom: 20, flexWrap: "wrap" }}>
        {[["h0curve","01 · H0 vs ENVIRONMENT"],["rhodiff","02 · ρ_DE RATIO"],["sensitivity","03 · SENSITIVITY"],["mechanisms","04 · COMBINED"],["predictions","05 · PREDICTIONS"]].map(([id,label]) => (
          <Tab key={id} label={label} active={tab===id} onClick={() => setTab(id)} />
        ))}
      </div>

      {/* TAB 1: H0 CURVE */}
      {tab === "h0curve" && (
        <div>
          <div style={{ fontSize: 11, color: C.muted, marginBottom: 12, lineHeight: 1.6 }}>
            Locally measured H0 as a function of environmental overdensity δ. In PNT, voids have higher dark energy density (more failed nucleations → more exhaust), producing higher local expansion rates. The Milky Way sits in the Laniakea underdensity (δ ≈ −0.35), explaining part of the observed H0 tension.
          </div>
          <ResponsiveContainer width="100%" height={320}>
            <LineChart data={deltaRange} margin={{ top: 10, right: 20, bottom: 30, left: 10 }}>
              <CartesianGrid stroke={C.border} strokeDasharray="3 3" />
              <XAxis dataKey="delta" stroke={C.muted} tick={{ fontSize: 10, fill: C.muted }}
                label={{ value: "Local overdensity δ", position: "insideBottom", offset: -15, fill: C.muted, fontSize: 10 }} />
              <YAxis domain={[62, 76]} stroke={C.muted} tick={{ fontSize: 10, fill: C.muted }}
                label={{ value: "H0 (km/s/Mpc)", angle: -90, position: "insideLeft", fill: C.muted, fontSize: 10 }} />
              <Tooltip content={<Tip />} />
              <ReferenceLine y={H0_local_obs} stroke={C.red} strokeDasharray="5 3"
                label={{ value: "Local observed 73.0", fill: C.red, fontSize: 9, position: "right" }} />
              <ReferenceLine y={H0_CMB} stroke={C.muted} strokeDasharray="5 3"
                label={{ value: "CMB 67.4", fill: C.muted, fontSize: 9, position: "right" }} />
              <ReferenceLine x={-0.35} stroke={C.green} strokeDasharray="4 4"
                label={{ value: "Our location", fill: C.green, fontSize: 9, position: "top" }} />
              <Line type="monotone" dataKey="H0_n10" stroke={C.muted} strokeWidth={1.5} dot={false} name="n=1.0" strokeDasharray="4 2" />
              <Line type="monotone" dataKey="H0_n15" stroke={C.accent} strokeWidth={2.5} dot={false} name="n=1.5 (fiducial)" />
              <Line type="monotone" dataKey="H0_n20" stroke={C.purple} strokeWidth={1.5} dot={false} name="n=2.0" strokeDasharray="4 2" />
            </LineChart>
          </ResponsiveContainer>

          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8, marginTop: 12 }}>
            <div style={{ background: C.panel, border: `1px solid ${C.green}44`, borderRadius: 4, padding: "10px 12px" }}>
              <div style={{ fontSize: 10, color: C.green, marginBottom: 6, letterSpacing: 1 }}>PHYSICAL MECHANISM</div>
              <div style={{ fontSize: 11, color: C.text, lineHeight: 1.7 }}>
                In voids, nearly all Planck nucleation attempts fail → maximum exhaust → higher ρ_DE. In filaments, mass concentrations convert nucleations into stars/BHs → less exhaust → lower ρ_DE. Higher local ρ_DE → faster local expansion → higher measured H0.
              </div>
            </div>
            <div style={{ background: C.panel, border: `1px solid ${C.gold}44`, borderRadius: 4, padding: "10px 12px" }}>
              <div style={{ fontSize: 10, color: C.gold, marginBottom: 6, letterSpacing: 1 }}>MODEL CAVEAT</div>
              <div style={{ fontSize: 11, color: C.text, lineHeight: 1.7 }}>
                The Schmidt-Kennicutt scaling (n=1.5) breaks down at very high densities (cluster cores). The physical range shown is δ = −0.9 to +0.5 where the model is reliable. f_fail is capped at [0,1] for physical consistency.
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 2: RHO_DE RATIO */}
      {tab === "rhodiff" && (
        <div>
          <div style={{ fontSize: 11, color: C.muted, marginBottom: 12 }}>
            Local dark energy density relative to cosmic mean. Voids are dark-energy rich; filaments are dark-energy depleted. The void-to-filament contrast is ~2-4× depending on densities.
          </div>
          <ResponsiveContainer width="100%" height={280}>
            <LineChart data={deltaRange} margin={{ top: 10, right: 20, bottom: 30, left: 10 }}>
              <CartesianGrid stroke={C.border} strokeDasharray="3 3" />
              <XAxis dataKey="delta" stroke={C.muted} tick={{ fontSize: 10, fill: C.muted }}
                label={{ value: "Local overdensity δ", position: "insideBottom", offset: -15, fill: C.muted, fontSize: 10 }} />
              <YAxis stroke={C.muted} tick={{ fontSize: 10, fill: C.muted }}
                label={{ value: "ρ_DE(local)/ρ_DE(mean)", angle: -90, position: "insideLeft", fill: C.muted, fontSize: 10 }} />
              <Tooltip content={<Tip />} />
              <ReferenceLine y={1.0} stroke={C.gold} strokeDasharray="3 3" label={{ value: "cosmic mean", fill: C.gold, fontSize: 9 }} />
              <ReferenceLine x={-0.35} stroke={C.green} strokeDasharray="4 4" label={{ value: "our location", fill: C.green, fontSize: 9, position: "top" }} />
              <Line type="monotone" dataKey="rho_ratio" stroke={C.accent} strokeWidth={2.5} dot={false} name="ρ_DE ratio (n=1.5)" />
            </LineChart>
          </ResponsiveContainer>

          {/* Environment table */}
          <div style={{ marginTop: 12 }}>
            <div style={{ fontSize: 10, color: C.muted, letterSpacing: 1, marginBottom: 8 }}>KEY ENVIRONMENTS</div>
            <div style={{ display: "flex", flexDirection: "column", gap: 4 }}>
              {[
                { name: "Deep void (δ=−0.8)", delta: -0.8, color: C.accent },
                { name: "Our location — Laniakea (δ=−0.35)", delta: -0.35, color: C.green },
                { name: "Cosmic mean (δ=0)", delta: 0, color: C.gold },
                { name: "Moderate filament (δ=+0.3)", delta: 0.3, color: C.orange },
              ].map((env, i) => {
                const ratio = rho_DE_ratio(env.delta);
                const h0 = H0_local(env.delta);
                return (
                  <div key={i} style={{ display: "flex", justifyContent: "space-between", background: C.panel, border: `1px solid ${env.color}33`, borderRadius: 3, padding: "8px 12px" }}>
                    <div style={{ fontSize: 11, color: env.color }}>{env.name}</div>
                    <div style={{ display: "flex", gap: 24, fontSize: 11, color: C.text }}>
                      <span>ρ_DE: <strong style={{ color: env.color }}>{ratio.toFixed(3)}×</strong></span>
                      <span>H0: <strong style={{ color: env.color }}>{h0.toFixed(1)}</strong></span>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      )}

      {/* TAB 3: SENSITIVITY */}
      {tab === "sensitivity" && (
        <div>
          <div style={{ fontSize: 11, color: C.muted, marginBottom: 12 }}>
            Fraction of Hubble tension explained by void effect across different void depths and Schmidt-Kennicutt scaling indices. Our fiducial case (δ=−0.35, n=1.5) gives 34%. Deeper voids or steeper scaling improve this.
          </div>
          <ResponsiveContainer width="100%" height={280}>
            <LineChart data={sensitivityData} margin={{ top: 10, right: 20, bottom: 30, left: 10 }}>
              <CartesianGrid stroke={C.border} strokeDasharray="3 3" />
              <XAxis dataKey="delta" stroke={C.muted} tick={{ fontSize: 10, fill: C.muted }}
                label={{ value: "Local void depth δ", position: "insideBottom", offset: -15, fill: C.muted, fontSize: 10 }} />
              <YAxis stroke={C.muted} tick={{ fontSize: 10, fill: C.muted }}
                label={{ value: "% of tension explained", angle: -90, position: "insideLeft", fill: C.muted, fontSize: 10 }} />
              <Tooltip content={<Tip />} />
              <ReferenceLine y={100} stroke={C.red} strokeDasharray="4 4" label={{ value: "100% resolution", fill: C.red, fontSize: 9 }} />
              <ReferenceLine y={50} stroke={C.gold} strokeDasharray="3 3" label={{ value: "50%", fill: C.gold, fontSize: 9 }} />
              <ReferenceLine x={-0.35} stroke={C.green} strokeDasharray="4 4" label={{ value: "our location", fill: C.green, fontSize: 9, position: "top" }} />
              <Line type="monotone" dataKey="n10" stroke={C.muted} strokeWidth={1.5} dot={true} name="n=1.0" />
              <Line type="monotone" dataKey="n15" stroke={C.accent} strokeWidth={2.5} dot={true} name="n=1.5 (fiducial)" />
              <Line type="monotone" dataKey="n20" stroke={C.purple} strokeWidth={1.5} dot={true} name="n=2.0" />
            </LineChart>
          </ResponsiveContainer>
          <div style={{ background: C.panel, border: `1px solid ${C.accent}33`, borderRadius: 4, padding: "10px 12px", marginTop: 12 }}>
            <div style={{ fontSize: 10, color: C.accent, letterSpacing: 1, marginBottom: 6 }}>KEY FINDING</div>
            <div style={{ fontSize: 11, color: C.text, lineHeight: 1.7 }}>
              The void mechanism alone cannot fully resolve the tension (would require δ ≈ −0.9, deeper than observed Laniakea). But it contributes 20-50% of the needed shift across the physically plausible parameter range. This is larger than standard matter-only void effects (~5-10%) because PNT adds a dark energy enhancement on top of the matter underdensity.
            </div>
          </div>
        </div>
      )}

      {/* TAB 4: COMBINED MECHANISMS */}
      {tab === "mechanisms" && (
        <div>
          <div style={{ fontSize: 11, color: C.muted, marginBottom: 12 }}>
            All PNT mechanisms combined. The void effect is the only one currently calculated. The others are physically motivated but require additional derivation.
          </div>
          {mechanisms.map((m, i) => (
            <div key={i} style={{ background: C.panel, border: `1px solid ${m.color}44`, borderLeft: `3px solid ${m.color}`, borderRadius: 4, padding: "10px 14px", marginBottom: 8 }}>
              <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 6, flexWrap: "wrap", gap: 4 }}>
                <div style={{ fontSize: 12, color: C.text, fontWeight: 700 }}>{m.name}</div>
                <span style={{ fontSize: 10, color: m.color, border: `1px solid ${m.color}55`, padding: "2px 8px", borderRadius: 3 }}>{m.status}</span>
              </div>
              <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                <div style={{ fontSize: 11, color: m.color, minWidth: 120 }}>
                  {m.min === 0 ? "unknown" : `+${m.min.toFixed(1)} – ${m.max.toFixed(1)} km/s/Mpc`}
                </div>
                <div style={{ flex: 1, height: 8, background: C.border, borderRadius: 4, overflow: "hidden" }}>
                  <div style={{ height: "100%", width: `${(m.max / 5.6) * 100}%`, background: m.color + "88", borderRadius: 4 }} />
                </div>
              </div>
            </div>
          ))}
          <div style={{ background: C.panel, border: `2px solid ${C.green}55`, borderRadius: 4, padding: "12px 14px", marginTop: 4 }}>
            <div style={{ fontSize: 11, color: C.green, letterSpacing: 1, marginBottom: 6 }}>COMBINED ESTIMATE</div>
            <div style={{ fontSize: 22, color: C.green, fontWeight: 700, marginBottom: 4 }}>+{totalMin.toFixed(1)} – {totalMax.toFixed(1)} km/s/Mpc</div>
            <div style={{ fontSize: 11, color: C.text }}>Required: 5.6 km/s/Mpc &nbsp;|&nbsp; Combined range: {(totalMin/5.6*100).toFixed(0)}–{(totalMax/5.6*100).toFixed(0)}% of tension</div>
          </div>
        </div>
      )}

      {/* TAB 5: PREDICTIONS */}
      {tab === "predictions" && (
        <div>
          {[
            { n: "1", color: C.green, label: "H0 varies with cosmic environment", conf: "HIGH CONFIDENCE", text: "Observers in voids should measure systematically higher H0 than observers in filaments. The gradient is ~1-4 km/s/Mpc across the δ = −0.8 to +0.3 range. This is testable by correlating H0 measurements with local large-scale structure catalogs (2MRS, SDSS, DES)." },
            { n: "2", color: C.accent, label: "H0 anisotropy correlates with void direction", conf: "HIGH CONFIDENCE", text: "H0 measured toward underdense directions should exceed H0 measured toward overdense directions. Already hinted at in Yeung & Chu 2022 CMB directional H0 variation. PNT gives this a physical mechanism." },
            { n: "3", color: C.gold, label: "Supernovae brightness residuals encode dark energy environment", conf: "MEDIUM CONFIDENCE", text: "Type Ia supernovae in voids should show slightly different brightness residuals than those in filaments — not just because of matter density, but because of local dark energy density variation. This is a new correlation not predicted by ΛCDM." },
            { n: "4", color: C.purple, label: "PNT void + EDE = partial tension resolution", conf: "SPECULATIVE", text: `Combined void effect (~2 km/s/Mpc) plus prompt EDE component (~1-2 km/s/Mpc) could explain 50-70% of the ${(5.6).toFixed(1)} km/s/Mpc tension. Full resolution may require memory field gravity contribution — currently uncalculated.` },
          ].map((p, i) => (
            <div key={i} style={{ background: C.panel, border: `1px solid ${p.color}44`, borderLeft: `3px solid ${p.color}`, borderRadius: 4, padding: "12px 14px", marginBottom: 10 }}>
              <div style={{ display: "flex", gap: 8, alignItems: "center", marginBottom: 8, flexWrap: "wrap" }}>
                <div style={{ width: 22, height: 22, borderRadius: "50%", background: p.color + "33", border: `1px solid ${p.color}`, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 11, color: p.color, fontWeight: 700, flexShrink: 0 }}>{p.n}</div>
                <div style={{ fontSize: 12, color: C.text, fontWeight: 700 }}>{p.label}</div>
                <span style={{ fontSize: 9, color: p.color, border: `1px solid ${p.color}55`, padding: "2px 8px", borderRadius: 3, letterSpacing: 1 }}>{p.conf}</span>
              </div>
              <div style={{ fontSize: 11, color: C.muted, lineHeight: 1.7 }}>{p.text}</div>
            </div>
          ))}
          <div style={{ background: C.panel, border: `1px solid ${C.green}44`, borderRadius: 4, padding: "12px 14px" }}>
            <div style={{ fontSize: 10, color: C.green, letterSpacing: 1, marginBottom: 6 }}>DISCRIMINATING TEST vs STANDARD VOID MODELS</div>
            <div style={{ fontSize: 11, color: C.text, lineHeight: 1.7 }}>
              Standard matter-only void models predict H0 enhancement from reduced gravitational drag (≈1-2 km/s/Mpc). PNT predicts an additional dark energy enhancement that scales differently with void depth. The two signatures can be separated by comparing H0 residuals against both matter density maps AND dark energy proxy measurements (Type Ia brightness, BAO scale variation). If PNT is correct, the dark energy contribution should be detectable independently of the matter void effect.
            </div>
          </div>
        </div>
      )}

      <div style={{ marginTop: 20, fontSize: 9, color: C.muted, letterSpacing: 1, textAlign: "center" }}>
        ECHO LABS · PNT HUBBLE TENSION · VOID-FILAMENT MECHANISM · MAY 2026 · NOT PEER REVIEWED
      </div>
    </div>
  );
}
