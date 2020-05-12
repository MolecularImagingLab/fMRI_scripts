#! /bin/bash

# This script will transfer files from the external hard drive to the local desktop computer
if [[ -z $1 ]]; then
	echo "---------------------------------"
	echo "please input subject ID [AVL-###]"
	echo "---------------------------------"
	exit
else
	echo "Pulling files from subject $1"
# Transfers event-related fMRI paradigm (.PAR) files
	scp -r /media/rami/My\ Passport/PAR_FILES/$1 /home/rami/Documents/PhD_Work/AVL/PAR_FILES
	echo "paradigm files successfully transferred"
# Transfers Go/No-Go (.CSV) result files
	scp -r /media/rami/My\ Passport/GONOGO/$1 /home/rami/Documents/PhD_Work/AVL/GONOGO
	echo "Go/No-Go result files successfully transferred"
# Transfers skin conductance recording (.acq and .txt) files
	scp -r /media/rami/My\ Passport/SCR/$1 /home/rami/Documents/PhD_Work/AVL/SCR
	echo "Skin conductance recording files successfully transferred"
fi
