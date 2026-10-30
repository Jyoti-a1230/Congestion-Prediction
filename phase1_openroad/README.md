# Phase 1: the open-source ASIC flow (OpenROAD + ORFS)

Goal: understand the RTL-to-GDS flow well enough to explain every stage, and to know what
routing congestion is and where it appears. Design used: `gcd` on the Nangate45 library.

## Toolchain (versions used)
| Item | Version |
|---|---|
| OS | WSL2, Ubuntu 22.04.5 (4 GB RAM, 16 GB swap, 2 cores) |
| OpenROAD | 26Q2-1164-g08f67ee5ec (prebuilt package) |
| Yosys | 0.69 (OSS CAD Suite) |
| KLayout | 0.30.12 |
| ORFS commit | 74b5f9610c107e9a155ac50e6eac4ad146e75344 |

Install guide: Part 2 article (link in the main README).

## What was done
- Ran the full flow stage by stage (`make synth`, `floorplan`, `place`, `cts`, `route`, `finish`).
- Traced where each cell came from by comparing the database after each stage
  (`scripts/dump_insts.tcl`).
- Swept the requested utilization and recorded the outcome (`results/utilization_sweep.csv`).

## Findings (details in `docs/phase1_findings.md`)
- The core is built from whole rows and sites, so the effective utilization differs from the request.
- Cell area grows through the flow (buffers, repair), so final utilization is much higher than at floorplan.
- At 72% and 75% requested utilization the flow failed in detailed placement inside the global-route
  stage, with about 1% free space left. gcd showed no routing overflow in any run that finished.
