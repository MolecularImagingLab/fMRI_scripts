#!/bin/bash
export PATH=$PATH:$PWD:/group/tuominen/EmoSal/scripts/

subj=$1
parbytime.py $subj
mk_recon.sh $subj
pre_proc.sh $subj
mk1stlev.sh $subj
