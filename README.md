# fMRI Scripts - Guideline for processing data at the Institute of Mental Health Research
## General fMRI data analysis scripts (.sh) to be used in conjunction with freesurfer as well as .py scripts for non-corrected region of interest analysis

## Aversive Conditioning (AVL) fMRI Analysis

## Transfer relevant fear conditioning files from data collection laptop to local desktop
    1. Insert usb external drive into the laptop (i.e. ‘My Passport’ on terminal)
    2. Open terminal and type: 
        I. cd /home/rami/Documents/fMRI_scripts OR your designated scripts folder
        II. ./transferfiles.sh [AVL-###]
            a) This transfers event-related paradigm (.PAR) from fear-conditioning task and Go/No-Go results (.CSV) files to the appropriate folders in “Heinrich”
    3. Unplug “Heinrich” from laptop and plug into desktop
    4. Open terminal and type: 
        I. cd /home/rami/Documents/fMRI_scripts OR your designated scripts folder
        II. ./pullfiles.sh [AVL-###]
            a) This transfers .PAR files, .CSV files, skin conductance recording (SCR) files (.acq and .txt) to the appropriate folders in the local desktop

## Create the appropriate data structure in the Brain Imaging Centre cloud
    1. Open terminal and type:
        I. EmoSally
            a) This will bring you to the scripts folder
        II. ./mkfolders.sh [AVL-###]
            a) This will create the appropriate data structure

## Download MRI data from the brain imaging centre (BIC) cloud
    1. Compress and download the selected participant from https://download.bic.theroyal.ca/
        I. Select whole participant folder and press "Build images" then place in /home/rami/Downloads
    2. Open terminal and type:
        I. ./avl_move.sh [AVL-###]
            a) This unpacks the DICOM files, converts them into NiFTY files and then transfers them into the appropriate folders in the BIC cloud, along with .PAR, .CSV and .acq/.txt files

## Process the fMRI data (first-level analysis only)
    1. Open terminal and type:
        I. EmoSally
            a) This will bring you to the scripts folder
        II. ./mkall.sh
            a) This will complete first-level analysis per subject using the following scripts: parbytime.py, mk_recon.sh, pre_proc.sh, mk1stlev.sh

## Use region-of-interest approach to see changes in fMRI activation
	1. Open terminal and type:
		I. EmoSally
		    a) This will bring you to the scripts folder
		II. ./ROI_byrun.py
		    a) This will create a .CSV file containing % change fMRI activation in the following brain regions: Amygdala, Caudate, Hippocampus, Pallidum, Putamen, Thalamus and Nucleus Accumbens
