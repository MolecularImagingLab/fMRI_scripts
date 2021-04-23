#! /bin/bash
export SUBJECTS_DIR=/group/tuominen/EmoSal_ParMod/SUBJECTS_DIR

subjects=$( cat subjectlist.txt )
np=0

for i in ${subjects[@]}; do
segmentHA_T1.sh $i &
(( np++ ))
echo $i
if [ $np == 20 ]; then
	echo $np
	echo "waiting and setting np back to 0"
	wait
	np=0
fi
done
