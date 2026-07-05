# P4 OSF Export Checklist

**Track:** SOC-MZI awareness-modulated decoherence  
**Purpose:** Keep the P4 repository packet aligned with a future OSF or Registered Report submission

---

## 1. Core protocol files

- [ ] `SOC-MZI-01-preregistration.md`
- [ ] `materials-and-measures.md`
- [ ] `statistical-analysis-plan.md`
- [ ] `lab-collaboration-brief.md`

---

## 2. Simulation support files

- [ ] runnable visibility-decay simulation script
- [ ] model summary
- [ ] CSV outputs used for planning or falsification scaffolding
- [ ] source-code notes or reproducibility notes

Important boundary:

Simulation files should be labeled as planning / falsification support, not as empirical evidence.

---

## 3. Blinding and analysis integrity items

- [ ] analysis scripts hashed or version-locked before unblinding
- [ ] condition scrambling / QRNG assignment process documented
- [ ] adversarial analysis path described
- [ ] deviations-from-preregistration log template prepared

---

## 4. Materials and apparatus packet

- [ ] source and detector specification sheet
- [ ] phase stabilization and drift monitoring notes
- [ ] eye-tracking / EEG instrumentation notes
- [ ] sham and null-information task description
- [ ] exclusion and artifact thresholds

---

## 5. AI / synthetic observer arm

- [ ] SOC-AI-01 protocol note
- [ ] operational `A_AI` definition
- [ ] control conditions for random / irrelevant-task observers
- [ ] code path or simulation note if included in OSF packet

---

## 6. Reporting language check

Before export, verify that P4 wording consistently says:

- the protocol tests a **rate-law extension**,
- positive results would support the preregistered effect structure,
- null results would constrain or weaken the coupling term,
- no file claims theory confirmation in advance.

---

## 7. Recommended submission bundle order

1. preregistration protocol
2. materials and measures appendix
3. statistical analysis appendix
4. simulation support packet
5. lab collaboration brief
6. AI observer control note if ready
7. deviations / version notes

---

## 8. Claim boundary

This checklist exists to improve submission discipline and reproducibility.

It should not be read as evidence that the P4 hypothesis has already been confirmed.