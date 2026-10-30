# Predicting routing congestion from placement-stage features

Can a model look at a placed chip design and predict where routing will be congested, before
clock-tree synthesis and routing run? This repository documents the project in two phases.

**Status:** Phase 1 complete, Phase 2 in progress (EDA).

## Phase 1: learn the flow (done)
Ran the full open-source RTL-to-GDS flow (OpenROAD, ORFS, Yosys, KLayout) on a 6 GB Windows laptop,
studied each stage, and swept the requested utilization on a small design.
See `phase1_openroad/` and the two articles:
- Part 1: the flow walkthrough (link in `docs/references.md`)
- Part 2: installing WSL2 and the tools (link in `docs/references.md`)

| Requested utilization | Outcome (gcd) |
|---|---|
| 55% | finished, final utilization 73%, no overflow |
| 70% | finished, final utilization 89%, no overflow |
| 72% | failed in detailed placement (about 0.3% free space) |
| 75% | failed in detailed placement (about 1% free space) |
| 80% | failed in global placement (density check) |

## Phase 2: predict congestion (in progress)
- **Data:** CircuitNet-N28 (6 designs, 10,242 layouts). See `docs/data_card.md`.
- **Task:** predict the global router's congestion map from placement-stage feature maps
  (macro region, cell density, RUDY variants).
- **Plan:** simple baselines, then a U-Net, then optionally a graph model, all on the same
  design-level splits and metrics (NRMSE, SSIM, and precision/recall for overflow tiles).
- **Results:** TBD.

## Repository layout
```
src/congestion/     reusable code (data helpers, dataset, models, metrics)
notebooks/          day-by-day notebooks (EDA, baselines, training, error analysis)
tests/              unit tests (pytest)
data/               data instructions (the data itself is not in git)
docs/               data card, decisions, limitations, progress log, findings
phase1_openroad/    scripts and results from the OpenROAD flow work
reports/, results/  figures and metrics tables
models/             saved models (not in git)
```

## Setup
```
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
make test
```
Heavy training runs on Colab; clone this repository there.

## Limitations
See `docs/limitations.md`.

## License and data
Code: MIT (see `LICENSE`). CircuitNet data and code have their own terms; cite the CircuitNet paper.

## Author
Jyoti Adwani
