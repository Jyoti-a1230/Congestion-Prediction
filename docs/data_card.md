# Data card: CircuitNet-N28 (routability features)

Source: CircuitNet (https://github.com/circuitnet/CircuitNet). Paper: arXiv 2208.01040.

## What it is
- 6 designs (RISCY-a, RISCY-FPU-a, zero-riscy-a, RISCY-b, RISCY-FPU-b, zero-riscy-b), 28 nm,
  12,960 flow runs of which 10,242 layouts survived.
- Flow: Synopsys Design Compiler for synthesis and Cadence Innovus for physical design.

## Knobs varied per design (from the paper)
Clock frequency 50/200/500 MHz; macro count (3/4/5 for "a" designs, 13/14/15 for "b" designs);
utilization 70/75/80/85/90%; 3 macro placements; 8 power-mesh settings; filler insertion timing.

## Folders used
- `congestion/congestion_early_global_routing`, `congestion/congestion_global_routing`
  (each with `utilization_based` and `overflow_based`) : labels.
- `macro_region`, `cell_density`, `RUDY/*` : input features.

## Findings from EDA (update as they are confirmed)
- Map shapes vary: 315 distinct shapes. Resizing policy: TODO.
- Tiles above 1.0 are rare (at most 0.25% of tiles in any file); tiles at exactly 1.0 are common.
- Overflow appears mostly at 80% utilization and above.
- Survivors are not a random sample of the runs (see `limitations.md`).
- One sample has `mNone` in its name.

## To verify
- Exact meaning of the label values and how horizontal and vertical maps combine.
- Whether the inputs were extracted from a placement-stage or a post-routing DEF.
- License terms of the data (the code repository is BSD-3-Clause).
