#!/bin/bash

space='lh rh mni305'
contrast='csmpr001 csmpr002 csmpr003 csmpr004 csppr001 csppr002 csppr003 csppr004 cspspr001 cspspr002 cspspr003 cspspr004 csp_v_csmpr001 csp_v_csmpr002 csp_v_csmpr003 csp_v_csmpr004'
for c in ${contrast[@]}; do
for s in ${space[@]}; do
	
	d=/group/tuominen/EmoSal/group/fc.${s}/${c}

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
