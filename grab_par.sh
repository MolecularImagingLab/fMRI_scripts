#!/bin/bash
# Define subjects
subjects=$1
# Loop over subjects to create respective input and output file names
for s in ${subjects[@]}; do
  input_file=$(find /Users/ramihamati/Documents/PAR_FILES/$s -name "*.par")
  for inp in ${input_file[@]}; do
    ./par_mod.py $inp $inp.mod
  done
  ./par_sort.py $s
done
