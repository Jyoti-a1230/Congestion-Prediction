# Phase 1 findings (gcd, Nangate45)

TODO: fill in from `Day2_flow_notes.md` and `Day3_utilization_sweep.md`.

Known results:
- Whole flow about 122 s, peak memory 820 MB (55% run).
- 505 cells at synthesis, 628.292 um2; floorplan core 1082.886 um2 (23 rows x 177 sites).
- Utilization trail (55% request): 58% floorplan, 59% after endcaps, 68% after CTS, 73% final.
- Cell budget: 63 buffers added in placement (35 input and 18 output port buffers plus repair),
  14 buffers from timing repair at CTS, 5 clock buffers and 3 dummy-load inverters, 12 buffers
  after global route. Placement removed 15 synthesis buffers.
- Global route (55%): metal2 max usage 69.52%, total usage 23.45%, zero overflow.
