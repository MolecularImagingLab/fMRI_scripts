#!/bin/bash

list='lh rh mni305'
cd ../mkanalysis
for s in ${list[@]}; do
	isxconcat-sess -sf ../scripts/sessidlist -analysis fc.$s -all-contrasts -percent -o ../group -d ../subjects

done
