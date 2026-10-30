# Dump every instance name and its cell type from one stage of a run.
# Usage (from OpenROAD-flow-scripts/flow):
#   VARIANT=base STAGE=3_place openroad -exit dump_insts.tcl
read_db results/nangate45/gcd/$::env(VARIANT)/$::env(STAGE).odb
set fh [open /tmp/$::env(VARIANT)_$::env(STAGE).txt w]
foreach inst [[ord::get_db_block] getInsts] {
  puts $fh "[$inst getName] [[$inst getMaster] getName]"
}
close $fh
