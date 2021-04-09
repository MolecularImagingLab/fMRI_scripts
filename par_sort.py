#!/usr/bin/env python
#! /group/tuominen/anaconda3/bin/python

# Import libraries
import os, sys, shutil
import numpy as np

def grab_par(root):
    ''' Grab par files for specific subject. '''
    subject_id = sys.argv[1]
    filefolder = os.path.join(root, subject_id, 'par')
    print('Grabbing par files from:' + filefolder)
    results = []
    files = os.listdir(filefolder)
    for f in files:
        if f.endswith('.mod'):
            results.append(f)
    return results, subject_id

def organize_par(results):
    ''' Organize par files by time. '''
    x = results
    oresults = sorted (x, key = lambda x: int(x[21:29]))
    return oresults

def send_par(root, oresults, subject_id):
    ''' Send par files to appropriate task runs. '''
    for i,r in enumerate(oresults):
        run = str(i+1)
        item = os.path.join(root,subject_id,'par',r)
        target = os.path.join(root, subject_id, 'bold', run.zfill(3), 'fc.par')
        shutil.copy(item,target)
        print(item, 'copied to run:', run)

def main():
    # Hardcoded file path
    root = '/group/tuominen/EmoSal_ParMod/subjects/'
    # Execute functions
    results, subject_id = grab_par(root)
    oresults = organize_par(results)
    send_par(root, oresults, subject_id)
if __name__ == "__main__":
# execute only if run as a script
    main()
