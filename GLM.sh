#!/bin/bash

space='lh rh mni305'
contrast='csp_slope csp_offset csm_slope csm_offset csp_v_csm_slope csp_v_csm_offset'
for c in ${contrast[@]}; do
for s in ${space[@]}; do

	d=/group/tuominen/EmoSal_ParMod/group/fc.${s}/${c}

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
