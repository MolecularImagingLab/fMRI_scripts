#!/bin/bash
export SUBJECTS_DIR=/group/tuominen/EmoSal_ParMod/SUBJECTS_DIR

subjects=$( cat subjectlist.txt )
for i in ${subjects[@]}; do
  ./mk_recon.sh $i
# preproc-sess requires python 2.X
  ./pre_proc.sh $i
  ./mk1stlev.sh $i
done
