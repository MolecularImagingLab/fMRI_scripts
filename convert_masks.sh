#! /bin/bash

# This script will conform mask files to cespct.nii.gz files to allow for ROI calculations

seg=$1
fmri=$2

if [[ -z $seg ]]; then
	echo "---------------------------------"
	echo "please input atlas file [atlas.nii.gz]"
	echo "---------------------------------"
	exit
else
	echo "Conforming $seg"
fi

if [[ -z $fmri ]]; then
	echo "---------------------------------"
	echo "please input (% change) brain activation file [cespct.nii.gz]"
	echo "---------------------------------"
	exit
else
	echo "Using $fmri as a template"
	mri_label2vol --seg $seg --temp $fmri --o $seg.downsampled2fmri.nii.gz --regheader $seg
fi

