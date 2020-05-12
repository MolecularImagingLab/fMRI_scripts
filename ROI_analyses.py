#!/usr/bin/env python
#! /home/lauri/anaconda2/bin/python

#load libraries 
import os
import nibabel as nb
import numpy as np
import pandas as pd

class AtlasInfo():
    """ This object is just a container for all ROI atlas related info """
    
    SUBJECTS_DIR = os.environ['SUBJECTS_DIR']
    maskfile = SUBJECTS_DIR + '/fsaverage/mri.2mm/aseg.mgz'
    mask = nb.load(maskfile).get_fdata()
    rois = {'amy': (18,54), 'cau': (11,50), 'hip': (17,53), 'pal': (13,52), 'put': (12,51), 
             'tha' : (10,49),'vst':(26,58)}
    
    roisIdx = {}
    for k in rois.keys():
        roisIdx[('lh_'+ k)] = np.where(mask==rois[k][0])
        roisIdx[('rh_'+ k)] = np.where(mask==rois[k][1])
        
    roisCombined = {}
    for k in rois.keys():
        roisCombined[k] = np.where( (mask==rois[k][0]) | (mask==rois[k][1]))   

    def __init__(self):
        self.rois = self.rois
        self.roisCombined = self.roisCombined
        self.roinames = list(self.rois.keys())
        self.roisIdx = self.roisIdx

def findSubjects(folder, StartPattern):    
    """This function will find subjects from the folder, based on naming pattern and the sort the subjects """
    subjects = []
    files = os.listdir(folder)
    for f in files:
        if f.startswith(StartPattern):
            subjects.append(f)
            
    subjects.sort()
    return subjects

def CreateDF(atlas):
    """ This function will create a PD dataframe with ID + group + ROIs as column names"""
    cspCol = [r + '_csp' for r in atlas.roinames]
    csmCol = [r + '_csm' for r in atlas.roinames]
    
    columns = ['ID', 'Status'] + cspCol + csmCol
    df_ = pd.DataFrame( columns=columns)
    df_ = df_.reindex(sorted(df_.columns), axis=1)
    return df_ 

def fillDF(subjects, folder, atlas, df_) :
    """ This function will loop over subjects, extract ROI values and fill out the DF
    Needs a list of subjects, the folder where they are located and a DF as inputs """
    
    for s in subjects:
        check = os.path.join(folder + s + '/bold/fc.mni305/csp/cespct.nii.gz')
        if not os.path.isfile(check):
            return
        
        swdf = extractData(s, folder, atlas)
        frames = [df_, swdf]
        df_ = pd.concat(frames, sort=False)
        frames = [df_, swdf]
        df_ = pd.concat(frames, sort=False)
        store = []
                        #else: 
                            #continue
   
    return df_

def extractData(s, folder, atlas):
    """ This function will load subject's fMRI data and extract mean values from each ROI """
    store = [] 
    conditions = ['csp', 'csm']
    for k in atlas.roinames():         
        for c in conditions:
            filename = os.path.join(folder + s + '/bold/fc.mni305/' + c +'/cespct.nii.gz')
            fMRI = nb.load(filename).get_fdata()
            datapoint = np.mean( fMRI[atlas.roisCombined[k]] )
            store.append(datapoint)

    if int(s[-3:]) < 100:
        status='control'
    else:
        status='FDR'
        
    d = [s, status] + [str(i) for i in store]
    swdf=pd.DataFrame(data=[d] )
    return swdf

def writeDF(df_, dname, fname):
    """ This function will save the dataframe in the location defined by dname and fname"""
    date = pd.to_datetime('today').strftime("%d_%m_%Y_")
    date_stamp = os.path.join(dname + date + fname)
    df_.to_csv((date_stamp), index = True, header=True)          

def main():
    ## This stuff is hardcoded, change when needed
    folder = '/group/tuominen/EmoSal/subjects/'
    StartPattern = 'AVL'
    atlas = AtlasInfo()
    dname = '/group/tuominen/EmoSal/ROI/'
    fname = 'ROI_analysis.csv'
    
    # get subjects 
    subjects = findSubjects(folder, StartPattern)
    # create a dataframe
    df_ = CreateDF()
    # extract ROI info from each subject and put it into the dataframe
    data = fillDF(subjects, folder, atlas, df_)
    # save dataframe
    writeDF(data, dname, fname)
    
    
if __name__ == "__main__":
    # execute only if run as a script
    main()

