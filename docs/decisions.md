# Decision log
Format: date, decision, reason, alternatives considered.

- Oct 2026: Use prebuilt OpenROAD packages inside WSL2. Reason: building from source is too heavy
  for a 6 GB laptop.
- Oct 2026: Use ORFS commit matching the installed OpenROAD build. Reason: newer ORFS scripts called a
  command missing in the installed OpenROAD.
- Oct 2026: Use the public CircuitNet-N28 data for the ML phase. Reason: generating thousands of
  labeled runs is not feasible on this hardware.
- TODO: label definition (stage, utilization vs overflow, horizontal/vertical).
- TODO: split strategy (by design, by family).
- TODO: resize and normalization policy.
