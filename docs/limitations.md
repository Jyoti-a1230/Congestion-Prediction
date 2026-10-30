# Limitations (keep updating)

- Labels are the global router's congestion estimate, not the final detailed-routing outcome.
- Inputs may be derived from a late-stage DEF (to be verified), which would make the task easier
  than predicting from a true pre-CTS placement.
- Failed runs were removed (about 21%), and not at random: survivorship bias.
- Only 6 designs in 3 families; "a" and "b" versions may be related, so even leave-one-design-out
  splits may leak.
- Map sizes vary, so resizing changes the physical scale.
- Overflow tiles are extremely rare, so metrics must be chosen with care.
- Phase 1 used a very small design (gcd) that never showed routing overflow.
