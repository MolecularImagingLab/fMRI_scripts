#! /bin/bash

#this script will 1) convert DICOM files into NIFTY files then 2) transfer the T1 structural scan, fMRI fear-conditioning scans, neuromelanin scan, paradigm files, skin conductance text files and Go/No-Go result files#

host=rami@10.156.156.24
subj=$1
FILEPATH=/home/rami/Downloads/AVL_FMRI/LTU-EmoSal-$subj

if [[ -z $subj ]]; then
	echo "---------------------------------"
	echo "please input subject ID [AVL-###]"
	echo "---------------------------------"
	exit
fi

if ssh $host "test ! -d /group/tuominen/EmoSal/subjects/$subj"; then
	echo "-------------------------------------------------------"
	echo "the corresponding data structure in the BIC cloud does not exist"
	echo "-------------------------------------------------------"
	exit
fi
#unpacks DICOM files
	echo "unpacking DICOM files from $subj"
	untar=$(find /home/rami/Downloads -mtime 0 -name "*.tar.gz")
	tar -C /home/rami/Downloads/AVL_FMRI -xvzf $untar
#detox MEMPRAGE\ RMS --> MEMPRAGE_RMS
	echo "converting DICOM files into NiFTY files from $subj"
	cd $FILEPATH	
	for file in *' '*
	do
  		mv -- "$file" "${file// /_}"
	done
#function to chose the highest # scan file
	set_latest () {
  	eval "latest=\${$#}"
	}
#evaluate highest # scan files then convert and transfer them
	set_latest $FILEPATH/*MEMPRAGE_RMS
	mri_convert $latest/LTU-EmoSal-$subj-0010.dcm $latest/T1.nii
	scp $latest/T1.nii rami@10.156.156.24:/group/tuominen/EmoSal/subjects/$subj/anat/001
	echo "T1 scan successfully converted and tranferred"
	set_latest $FILEPATH/[00-20]*-fMRI_3mmIso_run1
	mri_convert $latest/LTU-EmoSal-$subj-0010.dcm $latest/f.nii
	scp $latest/f.nii rami@10.156.156.24:/group/tuominen/EmoSal/subjects/$subj/bold/001
	echo "Run 1 scan successfully converted and tranferred"
	set_latest $FILEPATH/[00-20]*-fMRI_3mmIso_run2
	mri_convert $latest/LTU-EmoSal-$subj-0010.dcm $latest/f.nii
	scp $latest/f.nii rami@10.156.156.24:/group/tuominen/EmoSal/subjects/$subj/bold/002
	echo "Run 2 scan successfully converted and tranferred"
	set_latest $FILEPATH/[00-20]*-fMRI_3mmIso_run3
	mri_convert $latest/LTU-EmoSal-$subj-0010.dcm $latest/f.nii
	scp $latest/f.nii rami@10.156.156.24:/group/tuominen/EmoSal/subjects/$subj/bold/003
	echo "Run 3 scan successfully converted and tranferred"
	set_latest $FILEPATH/[00-20]*-fMRI_3mmIso_run4
	mri_convert $latest/LTU-EmoSal-$subj-0010.dcm $latest/f.nii
	scp $latest/f.nii rami@10.156.156.24:/group/tuominen/EmoSal/subjects/$subj/bold/004
	echo "Run 4 scan successfully converted and tranferred"
	set_latest $FILEPATH/[00-20]*-goldStar_NM_ref36_phOS20
	mri_convert $latest/LTU-EmoSal-$subj-0010.dcm $latest/nm.nii
	scp $latest/nm.nii rami@10.156.156.24:/group/tuominen/EmoSal/subjects/$subj/nm/001
	echo "Neuromelanin scan successfully converted and tranferred"
#find and transfer relevant files for paradigm, recall, skin conductance recordings and go/nogo
	par=$(find /home/rami/Documents/PhD_Work/AVL/PAR_FILES/$subj -name "*.par")
	scp $par rami@10.156.156.24:/group/tuominen/EmoSal/subjects/$subj/par
	echo "Paradigm files successfully tranferred"
	recall=$(find /home/rami/Documents/PhD_Work/AVL/PAR_FILES/$subj -name "$subj.RECALL*")
	scp $recall rami@10.156.156.24:/group/tuominen/EmoSal/subjects/$subj/recall
	echo "Recall file successfully transferred"
	scr=$(find /home/rami/Documents/PhD_Work/AVL/SCR/$subj -name "*.txt")
	scp $scr rami@10.156.156.24:/group/tuominen/EmoSal/subjects/$subj/scr
	echo "Skin conductance recording files successfully transferred"
	gng=$(find /home/rami/Documents/PhD_Work/AVL/GONOGO/$subj -name "*.csv")
	scp $gng rami@10.156.156.24:/group/tuominen/EmoSal/subjects/$subj/gng
	echo "Go/No-Go files successfully transferred"

