#!/usr/bin/env python
# coding: utf-8

# In[5]:


#! /usr/bin/python3

#load libraries 
import os
import nibabel as nb
import numpy as np
from nilearn import plotting
import matplotlib as plt
import pandas as pd


# In[10]:


def main():
# This segment of the script will use\
# Aseg.mgz: (subcortical segmentation loaded with its corresponding colour table)\
# To create masks of ROIs then using cespct.nii.gz (% change in signal)\
# Will calculate the change in activation of subcortical regions for each partipant\

# Creates mask file using aseg.mgz\
    SUBJECTS_DIR = os.environ['SUBJECTS_DIR']
    maskfile = SUBJECTS_DIR + '/fsaverage/mri.2mm/aseg.mgz'
    mask = nb.load(maskfile).get_fdata()
# Defines regions of interest, conditions and runs\
    rois = {'amy': (18,54), 'cau': (11,50), 'hip': (17,53),  
            'pal': (13,52), 'put': (12,51), 
            'tha' : (10,49),'vst': (26,58)} 
    rois_names = ['amy_left', 'amy_right', 'cau_left', 'cau_right', 'hip_left', 'hip_right',
                 'pal_left','pal_right','put_left','put_right',
                 'tha_left','tha_right', 'vst_left', 'vst_right']
    conditions = ['csm', 'csp']
    runwise = ['pr001', 'pr002', 'pr003', 'pr004']
    subjects = []
# Creates a date-stamped folder to save the results of the analysis\ 
    root = '/home/rami/Documents/sync/EmoSal/subjects/'
    date = pd.to_datetime('today').strftime("%d_%m_%Y_")
    path = os.path.join('/home/rami/Documents/sync/EmoSal/reports/',date)
    if not os.path.isdir(path):
        os.mkdir(path)
# Retrieves subjects from directory\
    files = os.listdir(root)
    for f in files:
        if f.startswith('AVL'):
            subjects.append(f)
    print('Analyzing data from:')
    subjects.sort()
    print(subjects)
# Creates a pandas dataframe with ID + group + ROIs as column names\
    columns = ['ID', 'Status']
    col_values = []
    for x in rois_names:
        for c in conditions:
            for r in runwise:
                l = os.path.join(x + '_' + c + '_' + r)
                col_values.append(l)
    df = pd.DataFrame(columns=col_values)
    df_ = pd.DataFrame(columns=columns)
    df_ = pd.concat([df_, df],axis=1)
    df_ = df_.reindex(sorted(df_.columns), axis=1)
# Loops over the subjects, by region, then by condition, then by run\
# Then insert data points into dataframe\
    for s in subjects:
        store = [] 
        if int(s[-3:]) < 100:
            status='control'
        else:
            status='FDR'
        check = os.path.join('/home/rami/Documents/sync/EmoSal/subjects/' + s + '/bold/fc.mni305/csp/cespct.nii.gz')
        if os.path.isfile(check):
            print('file exists for:')
            print(s)
            for k in rois.keys():
                lhrh = rois[k]
                lhidx = np.where(mask==lhrh[0])
                rhidx = np.where(mask==lhrh[1])    
                for c in conditions:
                    for r in runwise:
                        filename = os.path.join(root + s + '/bold/fc.mni305/' + r + '/' + c +'/cespct.nii.gz')
                        fMRI = nb.load(filename).get_fdata()
                        leftpoint = np.mean(fMRI[lhidx])
                        store.append(leftpoint)
                    for r in runwise:
                        filename = os.path.join(root + s + '/bold/fc.mni305/' + r + '/' + c +'/cespct.nii.gz')
                        fMRI = nb.load(filename).get_fdata()
                        rightpoint = np.mean(fMRI[rhidx])
                        store.append(rightpoint)
                        if len(store) == 112:
                            g = [s, status]  
                            d = g + store
                            swdf=pd.DataFrame(data=[d],columns=df_.columns)
                            frames = [df_, swdf]
                            df_ = pd.concat(frames, sort=False)
# Saves pandas dataframe as a csv in the date-stamped file path\
                            date_stamp = os.path.join(path, date + 'ROI_analysis_byrun.csv')
                            print(date_stamp)
                            df_.to_csv((date_stamp), index = True, header=True)
                            g = []
                            store = []
if __name__ == "__main__":
    # execute only if run as a script
    main()


# In[ ]:




