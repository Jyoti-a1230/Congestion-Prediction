#!/usr/bin/env bash
# Run only the floorplan stage for several requested utilizations and print what the tool built.
# Usage (from OpenROAD-flow-scripts/flow): bash floorplan_sweep.sh
for u in 66 68 69 70 71 72 73 74 75 76 78; do
  make FLOW_VARIANT=fp$u CORE_UTILIZATION=$u floorplan > /dev/null 2>&1
  echo -n "$u: "
  grep -h "Added\|Core area:\|Effective" logs/nangate45/gcd/fp$u/2_1_floorplan.log | tr -s ' ' | tr '\n' ' '
  echo
done
