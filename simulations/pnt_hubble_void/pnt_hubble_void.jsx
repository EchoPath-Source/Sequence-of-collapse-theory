import { useState } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, ReferenceLine } from "recharts";

const C = {
  bg: "#040d1a", panel: "#071428", border: "#0d2444",
  accent: "#00c8ff", gold: "#f0a500", green: "#00e5a0",
  red: "#ff4466", purple: "#a855f7", text: "#c8dff0",
  muted: "#4a6a8a", orange: "#ff8c00",
};

// PNT toy model: void-filament dark energy differential.
// rho_DE(delta) / rho_DE_mean = f_fail(delta) / f_fail_mean
// f_fail(delta) = 1 - f_succ_mean * max(0, 1 + delta)^n
// Physical cap: f_fail in [0, 1]

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

const deltaRange = [];
for (let d = -0.90; d <= 0.50; d += 0.05) {
  const d_r = parseFloat(d.toFixed(2));
  deltaRange.push({
    delta: d_r,
    H0_n15: parseFloat(H0_local(d_r).toFixed(3)),
    H0_n10: parseFloat(H0_local(d_r, 1.0).toFixed(3)),
    H0_n20: parseFloat(H0_local(d_r, 2.0).toFixed(3)),
    rho_ratio: parseFloat(rho_DE_ratio(d_r).toFixed(4)),
    H0_obs: H0_local_obs,
    H0_cmb: H0_CMB,
  });
}

const sensitivityData = [
  { delta: -0.20, n10: 14.5, n15: 20.5, n20: 25.9 },
  { delta: -0.30, n10: 21.6, n15: 29.8, n20: 36.5 },
  { delta: -0.35, n10: 25.2, n15: 34.1, n20: 41.3 },
  { delta: -0.40, n10: 28.8, n15: 38.3, n20: 45.7 },
  { delta: -0.50, n10: 35.8, n15: 46.1, n20: 53.4 },
];

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

      {tab === "h0curve" && (
        <div>
          <div style={{ fontSize: 11, color: C.muted, marginBottom: 12, lineHeight: 1.6 }}>
            Locally measured H0 as a function of environmental overdensity δ. In PNT, voids have higher dark energy density (more failed nucleations → more exhaust), producing higher local expansion rates. A representative local underdensity δ ≈ −0.35 explains part of the observed H0 tension.
          </div>
          <ResponsiveContainer width="100%" height={320}>
            <LineChart data={deltaRange} margin={{ top: 10, right: 20, bottom: 30, left: 10 }}>
              <CartesianGrid stroke={C.border} strokeDasharray="3 3" />
              <XAxis dataKey="delta" stroke={C.muted} tick={{ fontSize: 10, fill: C.muted }}
                label={{ value: "Local overdensity δ", position: "insideBottom", offset: -15, fill: C.muted, fontSize: 10 }} />
              <YAxis domain={[62, 76]} stroke={C.muted} tick={{ fontSize: 10, fill: C.muted }}
                label={{ value: "H0 (km/s/Mpc)", angle: -90, position: "insideLeft", fill: C.muted, fontSize: 10 }} />
              <Tooltip content={<Tip />} />
              <ReferenceLine y={H0_local_obs} stroke={C.red} strokeDasharray="5 3" label={{ value: "Local observed 73.0", fill: C.red, fontSize: 9, position: "right" }} />
              <ReferenceLine y={H0_CMB} stroke={C.muted} strokeDasharray="5 3" label={{ value: "CMB 67.4", fill: C.muted, fontSize: 9, position: "right" }} />
              <ReferenceLine x={-0.35} stroke={C.green} strokeDasharray="4 4" label={{ value: "Representative local δ", fill: C.green, fontSize: 9, position: "top" }} />
              <Line type="monotone" dataKey="H0_n10" stroke={C.muted} strokeWidth={1.5} dot={false} name="n=1.0" strokeDasharray="4 2" />
              <Line type="monotone" dataKey="H0_n15" stroke={C.accent} strokeWidth={2.5} dot={false} name="n=1.5 (fiducial)" />
              <Line type="monotone" dataKey="H0_n20" stroke={C.purple} strokeWidth={1.5} dot={false} name="n=2.0" strokeDasharray="4 2" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      )}

      {tab === "rhodiff" && (
        <div>
          <div style={{ fontSize: 11, color: C.muted, marginBottom: 12 }}>
            Local dark energy density relative to cosmic mean. Voids are dark-energy rich; filaments are dark-energy depleted in the PNT toy model.
          </div>
          <ResponsiveContainer width="100%" height={280}>
            <LineChart data={deltaRange} margin={{ top: 10, right: 20, bottom: 30, left: 10 }}>
              <CartesianGrid stroke={C.border} strokeDasharray="3 3" />
              <XAxis dataKey="delta" stroke={C.muted} tick={{ fontSize: 10, fill: C.muted }} label={{ value: "Local overdensity δ", position: "insideBottom", offset: -15, fill: C.muted, fontSize: 10 }} />
              <YAxis stroke={C.muted} tick={{ fontSize: 10, fill: C.muted }} label={{ value: "ρ_DE(local)/ρ_DE(mean)", angle: -90, position: "insideLeft", fill: C.muted, fontSize: 10 }} />
              <Tooltip content={<Tip />} />
              <ReferenceLine y={1.0} stroke={C.gold} strokeDasharray="3 3" label={{ value: "cosmic mean", fill: C.gold, fontSize: 9 }} />
              <ReferenceLine x={-0.35} stroke={C.green} strokeDasharray="4 4" label={{ value: "representative local δ", fill: C.green, fontSize: 9, position: "top" }} />
              <Line type="monotone" dataKey="rho_ratio" stroke={C.accent} strokeWidth={2.5} dot={false} name="ρ_DE ratio (n=1.5)" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      )}

      {tab === "sensitivity" && (
        <div>
          <div style={{ fontSize: 11, color: C.muted, marginBottom: 12 }}>
            Fraction of Hubble tension explained by void effect across different void depths and scaling indices. Fiducial case δ=−0.35, n=1.5 gives ~34%.
          </div>
          <ResponsiveContainer width="100%" height={280}>
            <LineChart data={sensitivityData} margin={{ top: 10, right: 20, bottom: 30, left: 10 }}>
              <CartesianGrid stroke={C.border} strokeDasharray="3 3" />
              <XAxis dataKey="delta" stroke={C.muted} tick={{ fontSize: 10, fill: C.muted }} label={{ value: "Local void depth δ", position: "insideBottom", offset: -15, fill: C.muted, fontSize: 10 }} />
              <YAxis stroke={C.muted} tick={{ fontSize: 10, fill: C.muted }} label={{ value: "% of tension explained", angle: -90, position: "insideLeft", fill: C.muted, fontSize: 10 }} />
              <Tooltip content={<Tip />} />
              <ReferenceLine y={100} stroke={C.red} strokeDasharray="4 4" label={{ value: "100% resolution", fill: C.red, fontSize: 9 }} />
              <ReferenceLine y={50} stroke={C.gold} strokeDasharray="3 3" label={{ value: "50%", fill: C.gold, fontSize: 9 }} />
              <ReferenceLine x={-0.35} stroke={C.green} strokeDasharray="4 4" label={{ value: "representative local δ", fill: C.green, fontSize: 9, position: "top" }} />
              <Line type="monotone" dataKey="n10" stroke={C.muted} strokeWidth={1.5} dot={true} name="n=1.0" />
              <Line type="monotone" dataKey="n15" stroke={C.accent} strokeWidth={2.5} dot={true} name="n=1.5 (fiducial)" />
              <Line type="monotone" dataKey="n20" stroke={C.purple} strokeWidth={1.5} dot={true} name="n=2.0" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      )}

      {tab === "mechanisms" && (
        <div>
          {mechanisms.map((m, i) => (
            <div key={i} style={{ background: C.panel, border: `1px solid ${m.color}44`, borderLeft: `3px solid ${m.color}`, borderRadius: 4, padding: "10px 14px", marginBottom: 8 }}>
              <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 6, flexWrap: "wrap", gap: 4 }}>
                <div style={{ fontSize: 12, color: C.text, fontWeight: 700 }}>{m.name}</div>
                <span style={{ fontSize: 10, color: m.color, border: `1px solid ${m.color}55`, padding: "2px 8px", borderRadius: 3 }}>{m.status}</span>
              </div>
              <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                <div style={{ fontSize: 11, color: m.color, minWidth: 120 }}>{m.min === 0 ? "unknown" : `+${m.min.toFixed(1)} – ${m.max.toFixed(1)} km/s/Mpc`}</div>
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

      {tab === "predictions" && (
        <div>
          <div style={{ background: C.panel, border: `1px solid ${C.green}44`, borderRadius: 4, padding: "12px 14px" }}>
            <div style={{ fontSize: 10, color: C.green, letterSpacing: 1, marginBottom: 6 }}>DISCRIMINATING TEST vs STANDARD VOID MODELS</div>
            <div style={{ fontSize: 11, color: C.text, lineHeight: 1.7 }}>
              Standard matter-only void models predict H0 enhancement from reduced gravitational drag. PNT predicts an additional dark-energy enhancement that scales differently with void depth. The two signatures can be separated by comparing H0 residuals against both matter-density maps and dark-energy proxy measurements such as Type Ia supernova residuals and BAO scale variation.
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
