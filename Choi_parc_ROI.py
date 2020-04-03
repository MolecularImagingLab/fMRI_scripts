#!/usr/bin/env python
# coding: utf-8

# In[1]:


#! /usr/bin/python3

#load libraries 
import os
import nibabel as nb
import numpy as np
from nilearn import plotting
from nilearn import datasets
from nilearn import image
import matplotlib as plt
import pandas as pd


# In[7]:


def main():
# This segment of the script will use\
# Choi2012_7Networks_MNI152_FreeSurferConformed1mm_TightMask.nii.gz downsampled to a 2mm fmri mask\
# To create masks of striatal subregions then using cespct.nii.gz (% change in signal)\
# Will calculate the change in activation of striatal subregions for each partipant\

# Creates mask file using Choi 2012 tight mask\
    maskfile = '/home/lauri/Documents/temp/Choi_JNeurophysiol12_MNI152/Choi2012_7Networks_MNI152_FreeSurferConformed1mm_TightMask.nii.gz.downsampled2fmri.nii.gz'
    mask = nb.load(maskfile).get_fdata()
# Defines regions of interest, conditions and runs\
    rois = {'7Networks_1': 1, '7Networks_2': 2, '7Networks_3': 3,  
            '7Networks_4': 4, '7Networks_5': 5, 
            '7Networks_6' : 6,'7Networks_7': 7} 
    conditions = ['csm', 'csp']
    runwise = ['pr001', 'pr002', 'pr003', 'pr004']
    subjects = []
# Creates a date-stamped folder to save the results of the analysis\ 
    subjects_path = '/media/lauri/My Passport/My_Computer/Documents/sync_me/EmoSal/subjects'
    date = pd.to_datetime('today').strftime("%d_%m_%Y_")
    path = os.path.join('/media/lauri/My Passport/My_Computer/Documents/sync_me/EmoSal/reports/',date)
    if not os.path.isdir(path):
        os.mkdir(path)
# Retrieves subjects from directory\
    files = os.listdir(subjects_path)
    for f in files:
        if f.startswith('AVL'):
            subjects.append(f)
    print('Analyzing data from:')
    subjects.sort()
    print(subjects)
# Creates a pandas dataframe with ID + group + ROIs as column names\
    columns = ['ID', 'Status']
    col_values = []
    for k in rois.keys():
        for c in conditions:
            for r in runwise:
                l = os.path.join(k + '_' + c + '_' + r)
                col_values.append(l)
    df = pd.DataFrame(columns=col_values)
    df_ = pd.DataFrame(columns=columns)
    df_ = pd.concat([df_, df],axis=1)
# Loops over the subjects, by region, then by condition, then by run\
# Then insert data points into dataframe\
    for s in subjects:
        store = [] 
        if int(s[-3:]) < 100:
            status='control'
        else:
            status='FDR'
        check = os.path.join('/media/lauri/My Passport/My_Computer/Documents/sync_me/EmoSal/subjects/' + s + '/bold/fc.mni305/csp/cespct.nii.gz')
        if os.path.isfile(check):
            print('file exists for:')
            print(s)
            for k in rois:
                lhrh = rois[k]
                idx = np.where(mask==lhrh)
                for c in conditions:
                    for r in runwise:
                        filename = os.path.join('/media/lauri/My Passport/My_Computer/Documents/sync_me/EmoSal/subjects/' + s + '/bold/fc.mni305/' + r + '/' + c +'/cespct.nii.gz')
                        fMRI = nb.load(filename).get_fdata() 
                        point = np.mean(fMRI[idx])
                        store.append(point)
                        if len(store) == 56:
                            g = [s, status]  
                            d = g + store
                            swdf=pd.DataFrame(data=[d],columns=df_.columns)
                            frames = [df_, swdf]
                            df_ = pd.concat(frames, sort=False)
# Saves pandas dataframe as a csv in the date-stamped file path\
                            date_stamp = os.path.join(path, date + 'striatal_analysis_byrun.csv')
                            print(date_stamp)
                            df_.to_csv((date_stamp), index = False, header=True)
                            g = []
                            store = []
if __name__ == "__main__":
    # execute only if run as a script
    main()

