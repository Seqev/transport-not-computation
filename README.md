# Transport, Not Computation







[![DOI](https://zenodo.org/badge/1259663522.svg)](https://doi.org/10.5281/zenodo.20547457)







**Umbrella + review for a falsification program on how 1B–3B language models use long context.**
Evgenii Vyaltsev (ORCID 0009-0004-3712-6798), Daniil Vyaltsev — June 2026.

<!-- After Zenodo mint: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX) -->

Four independent, pre-registered, matched-control causal gates — on attention, on the repair of
retrieval failure, on multi-hop synthesis, and on a directly-optimized latent state — converge,
cross-model (Llama-3.2-1B/3B, Qwen2.5-3B), on one regime-bounded thesis:

> **the network delivers, and composes only through an external buffer; it does not latently
> compute — and a latent computation state cannot be optimized into existence.**

- **`PROGRAM.md`** — the one-page map (thesis, substrate, four gates, what's closed/survived/open,
  product corollary, method, artifact table with DOIs). Start here.
- **`transport_not_computation_review.pdf`** — the full review paper (7 pp).
- **`make_figures.py`** — regenerates the two figures (program arc; four-gate signature).

This umbrella references the **verified headline numbers** from the six constituent releases;
each of those repositories holds its own raw logs, pre-registration, and reproduction script.

## Reproduce
```bash
python3 -m pip install matplotlib numpy
python3 make_figures.py
pdflatex transport_not_computation_review.tex && pdflatex transport_not_computation_review.tex
```

## The program (constituent repositories)
1. `qaxis-exact-scaling` — exact ranking + entropy-concentration scaling
2. `dcr-retention-no-kcrit` — no critical key budget (DOI 10.5281/zenodo.20514229)
3. `retrieval-arc-delivery` — the bottleneck is delivery
4. `synthesis-is-transport` — even synthesis is transport
5. `latent-scratchpad-search` — no latent scratchpad
6. `matched-magnitude-controls` — the method (DOI 10.5281/zenodo.20261207)

## Scope (strict)
1B–3B, retrieval and synthetic synthesis, greedy, N≤128K (synthesis N=4096). Every NULL is
"not at this scale on this design", not "never". The thesis does not transfer up the scale.

## License
Text/figures: CC-BY-4.0. Code: MIT.

## Citation
See `CITATION.cff`; full BibTeX added once the Zenodo DOI is minted.
