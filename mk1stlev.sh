cd ../mkanalysis
space='lh rh mni305'
for s in ${space[@]}; do 
selxavg3-sess -s $1 -analysis fc.${s} -run-wise -d ../subjects
selxavg3-sess -s $1 -analysis fc.${s} -d ../subjects
done
