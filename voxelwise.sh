#!/bin/bash

#Run GLM on all 4 runs
cd /media/lauri/heinrich/My_Computer/Documents/sync_me/EmoSal/group/fc.mni305/csp_v_csm/AVL_GLM.wls/osgm

mri_glmfit \
--y ../../cespct.nii.gz \
--fsgd avl.fsgd dods \
--C nm_contrast.mtx \
--no-cortex \
--glmdir voxelwise_dir

#Run GLM on each run separately 
runs='pr001 pr002 pr003 pr004'
for r in ${runs[@]}; do

	cd /media/lauri/heinrich/My_Computer/Documents/sync_me/EmoSal/group/fc.mni305/csp_v_csm/$r/AVL_GLM.wls/osgm
	
	mri_glmfit \
	--y ../../cespct.nii.gz \
	--fsgd avl.fsgd dods \
	--C nm_contrast.mtx \
	--no-cortex \
	--glmdir voxelwise_dir
done
