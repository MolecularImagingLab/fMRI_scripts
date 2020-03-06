#!/usr/bin/env python
# coding: utf-8

# In[1]:


#! /home/lauri/anaconda2/bin/python

#load libraries 
import os
import nibabel as nb
import numpy as np
from nilearn import plotting
import matplotlib as plt
import pandas as pd


# In[7]:


def main():
    # set paths 
    # load mri.2mm/aseg.mgz
    ## set-up environment
    SUBJECTS_DIR = os.environ['SUBJECTS_DIR']
    ## load mask file using nibabel
    maskfile = SUBJECTS_DIR + '/fsaverage/mri.2mm/aseg.mgz'
    mask = nb.load(maskfile).get_data()
    print('The dimensions of the mask are:') 
    print(mask.shape)
    
    # roi definitions
    rois = {'amy': (18,54), 'cau': (11,50), 'hip': (17,53), 'pal': (13,52), 'put': (12,51), 
             'tha' : (10,49),'vst':(26,58)} 
    roiss = rois.keys()
    print(roiss)
    
    # subjects
    subjects = []
    root = '/group/tuominen/EmoSal/subjects/'
    files = os.listdir(root)
    for f in files:
        if f.startswith('AVL'):
            subjects.append(f)
    print('Analyzing data from:')
    subjects.sort()
    print(subjects)
    
    # conditions 
    conditions=['csm', 'csp']
    
    # runs
    runwise=['pr001', 'pr002', 'pr003', 'pr004']
    
    #create a pandas dataframe with ID + group + ROIs as column names
    columns = ['ID', 'Status',
               (str(roiss[0] + '_csppr001')),(str(roiss[1]) + '_csppr001'),
          (str(roiss[2]) + '_csppr001'), (str(roiss[3]) + '_csppr001'),
          (str(roiss[4]) + '_csppr001'), (str(roiss[5]) + '_csppr001'),
          (str(roiss[6]) + '_csppr001'), (str(roiss[0] + '_csmpr001')),(str(roiss[1]) + '_csmpr001'),
          (str(roiss[2]) + '_csmpr001'), (str(roiss[3]) + '_csmpr001'),
          (str(roiss[4]) + '_csmpr001'), (str(roiss[5]) + '_csmpr001'),
          (str(roiss[6]) + '_csmpr001'), (str(roiss[0] + '_csppr002')),(str(roiss[1]) + '_csppr002'),
          (str(roiss[2]) + '_csppr002'), (str(roiss[3]) + '_csppr002'),
          (str(roiss[4]) + '_csppr002'), (str(roiss[5]) + '_csppr002'),
          (str(roiss[6]) + '_csppr002'), (str(roiss[0] + '_csmpr002')),(str(roiss[1]) + '_csmpr002'),
          (str(roiss[2]) + '_csmpr002'), (str(roiss[3]) + '_csmpr002'),
          (str(roiss[4]) + '_csmpr002'), (str(roiss[5]) + '_csmpr002'),
          (str(roiss[6]) + '_csmpr002'), (str(roiss[0] + '_csppr003')),(str(roiss[1]) + '_csppr003'),
          (str(roiss[2]) + '_csppr003'), (str(roiss[3]) + '_csppr003'),
          (str(roiss[4]) + '_csppr003'), (str(roiss[5]) + '_csppr003'),
          (str(roiss[6]) + '_csppr003'), (str(roiss[0] + '_csmpr003')),(str(roiss[1]) + '_csmpr003'),
          (str(roiss[2]) + '_csmpr003'), (str(roiss[3]) + '_csmpr003'),
          (str(roiss[4]) + '_csmpr003'), (str(roiss[5]) + '_csmpr003'),
          (str(roiss[6]) + '_csmpr003'), (str(roiss[0] + '_csppr004')),(str(roiss[1]) + '_csppr004'),
          (str(roiss[2]) + '_csppr004'), (str(roiss[3]) + '_csppr004'),
          (str(roiss[4]) + '_csppr004'), (str(roiss[5]) + '_csppr004'),
          (str(roiss[6]) + '_csppr004'), (str(roiss[0] + '_csmpr004')),(str(roiss[1]) + '_csmpr004'),
          (str(roiss[2]) + '_csmpr004'), (str(roiss[3]) + '_csmpr004'),
          (str(roiss[4]) + '_csmpr004'), (str(roiss[5]) + '_csmpr004'),
          (str(roiss[6]) + '_csmpr004')]

    df_ = pd.DataFrame( columns=columns)
    df_ = df_.reindex(sorted(df_.columns), axis=1)
    
    #loop over subjects
    for s in subjects:
        store = [] 
        if int(s[-3:]) < 100:
            status='control'
        else:
            status='FDR'
        g= [s, status]  
        check = os.path.join('/group/tuominen/EmoSal/subjects/' + s + '/bold/fc.mni305/csp/cespct.nii.gz')
        if os.path.isfile(check):
            print('file exists for:')
            print(s)
    # create a new row for the subject, you may want to test if that row already exists, if so skip that subject
        # loop over ROIs
            for k in rois.keys():
                lhrh = rois[k]
                lhidx = np.where(mask==lhrh[0])
                rhidx = np.where(mask==lhrh[1])
        # loop over conditions and runs         
                for c in conditions:
                    for r in runwise:
                        filename = os.path.join(root + s + '/bold/fc.mni305/' + r + '/' + c +'/cespct.nii.gz')
                        fMRI = nb.load(filename).get_data()
                        datapoint = np.mean( np.concatenate( ( fMRI[lhidx], fMRI[rhidx] ) ) )
                        store.append(datapoint)
                        print(c)
                        print(r)
                        print(store)
        # put this data point to the right location in the dataframe
                        #for i in store:
                            #if len(store) >= 14:
            d = g + [str(i) for i in store]
            swdf=pd.DataFrame(data=[d] ,columns=columns)
            frames = [df_, swdf]
            df_ = pd.concat(frames, sort=False)
            store = []
                        #else: 
                            #continue
    # save pandas dataframe as a csv
    date = pd.to_datetime('today').strftime("%d_%m_%Y_")
    date_stamp = os.path.join('/group/tuominen/EmoSal/ROI/' + date + 'ROI_analysis_byrun.csv')
    print(date_stamp)
    df_.to_csv((date_stamp), index = True, header=True)          

if __name__ == "__main__":
    # execute only if run as a script
    main()

