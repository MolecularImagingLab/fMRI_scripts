#!/bin/bash

space='lh rh mni305'
contrast='csm csp csp_v_csm csps'
run='pr001 pr002 pr003 pr004'
for r in ${run[@]}; do
for c in ${contrast[@]}; do
for s in ${space[@]}; do
	
	d=/group/tuominen/EmoSal/group/fc.${s}/${c}/${r}

	if [ $s != 'mni305' ]; then
		conditional="--surface fsaverage  ${s}"
	else 
		conditional=''
	fi

	mri_glmfit --y ${d}/cespct.nii.gz \
	  --wls ${d}/cesvarpct.nii.gz \
	  --osgm \
	  --glmdir ${d}/AVL_GLM.wls \
	  --nii.gz \
	  ${conditional}

done
done 
done
