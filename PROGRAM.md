# Transport, Not Computation — program map

**One-page map of a falsification program on how 1B–3B language models use long context.**
Evgenii Vyaltsev (ORCID 0009-0004-3712-6798), Daniil Vyaltsev — June 2026.

---

## The thesis (regime-bounded: 1B–3B, two families, retrieval + synthetic synthesis, greedy)

> **The network DELIVERS, and composes only through an EXTERNAL buffer; it does not
> latently COMPUTE — and a latent computation state cannot be optimized into existence.**

Four independent, pre-registered, matched-control causal gates converge on this, cross-model
(Llama-3.2-1B/3B, Qwen2.5-3B). It is a **map of a boundary**, not a universal law: every NULL
is "not at this scale on this design", not "never".

---

## The substrate (clears the obvious confound)

- **Exact, training-free selector.** Ranking by ⟨u_Q,K_i⟩ (u_Q=Q/‖Q‖) is order-identical to the
  raw attention score → top-k is the *true* top-k, no approximation, no training.
- **No critical key budget.** A 4× swing of the absolute budget moves retrieval accuracy ≤0.03 at
  any length, on 3 models. The compressor is **not** the limit — the base model is. Capacity, not
  budget, raises the ceiling (selected-yet-wrong at 32K: 0.37→0.23→0.18 from 1B→3B).
- **INT8 KV cache** at 0.508× footprint, +0.714% PPL. Entropy concentration H_N=α·log N+β (α≈0.31)
  → sublinear support, advantage strengthens with N (descriptive).

## The four gates

| gate | lever tested | decisive number | verdict |
|------|--------------|-----------------|---------|
| **γ — attention** | up-weight a key vs re-deliver it | re-delivery **100%** ≥ weight-gain **80%** | TRANSPORT |
| **delivery ladder** | shrink payload; transplant a learned state | **27B** binding **100%** vs bare code **58%**; state-transfer ties random controls | DELIVERY (no attention/state shortcut) |
| **synthesis** | corrupt each hop; block elimination | implicit mid-hop flip **0.05/0.11** vs CoT **0.84/0.90**; implicit floors to chance under decoys | RETRIEVAL + ELIMINATION; CoT = self-delivery |
| **latent scratchpad** | *optimize* a latent state to force composition (5 controls) | carries D with code-fact removed **0.94/0.81**; P(B) stays ~0; doesn't transfer | ANSWER-INJECTION, not composition |

## What's closed / survived / open

**Closed (controlled NULLs):** spectral causal mechanism · absolute K_crit · attention-redirection
memory class · transplanted state-skill / skill-library · internal multi-hop composition at 3B ·
optimizable latent composition state.

**Survived (positives):** exact training-free selector + scaling law · retention robustness
(budget-insensitive) · content-addressable delivery + 27-byte micro-hint floor · capacity-shifts-ceiling.

**Open:** internal composition *above* 3B / with trained chains · the exact channel of the
above-chance implicit signal (structural/elimination) · delocalization (answer survives physical
removal of the fact?).

## Product corollary (each component justified by a gate)

- **Engine:** exact selector + INT8 KV → longer context, lower memory on consumer hardware, at
  iso-ability. Sparsity buys speed/length, not intelligence.
- **Memory:** store attribute→code bindings (~27 B), retrieve, deliver freshly — RAG of micro-hints.
  No attention-steering, no skill-library adapter (both closed).
- **Composition:** externalize it (CoT / self-RAG). A learned "thinking" vector memorizes the
  answer; it does not reason.
- **"Smarter"** = capacity or better delivery/scaffolding, not the sparsity budget or an internal shortcut.

## Method (why the NULLs are trustworthy)

Pre-registered grids/thresholds/verdict-maps fixed before running; matched-magnitude controls;
paired within-run CIs; extra scrutiny for a positive after a NULL streak. The discipline reversed
its own false positives (a spectral "mechanism"; a 17%@n=12 transfer signal gone at n=60; a
wrong-layer false zero) and produced a reusable catch: under competition, node *removal* is
confounded by elimination — the faithful usage test is in-place *corruption*.

---

## Artifacts (each a standalone release with raw logs, pre-registration, figure script)

| # | title | repo | DOI |
|---|-------|------|-----|
| 1 | Exact ranking + entropy scaling | `qaxis-exact-scaling` | (mint) |
| 2 | No critical key budget (retention) | `dcr-retention-no-kcrit` | 10.5281/zenodo.20514229 |
| 3 | The bottleneck is delivery (retrieval arc) | `retrieval-arc-delivery` | (mint) |
| 4 | Even synthesis is transport | `synthesis-is-transport` | (mint) |
| 5 | No latent scratchpad | `latent-scratchpad-search` | (mint) |
| 6 | Matched-magnitude controls (method) | `matched-magnitude-controls` | 10.5281/zenodo.20261207 |
| — | **This umbrella / review** | `transport-not-computation` | (mint) |

Mint order for cross-DOIs: 1 → 3 → 4 → 5 → umbrella (each references the prior). Retention (2) and
the method note (6) already carry DOIs.
