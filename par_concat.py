#!/usr/bin/env python
#! /home/lauri/anaconda3/bin/python

import os, sys, glob, re
import pandas as pd
import numpy as np

# Define file paths
subjectpath = '/media/lauri/My Passport/My_Computer/Documents/sync_me/EmoSal/subjects'
subjects = os.listdir(subjectpath)
print(subjects)
# Grab par files
for s in subjects:
    parpath = os.path.join('/media/lauri/My Passport/My_Computer/Documents/sync_me/EmoSal/subjects',s,'par')
    files=os.listdir(parpath)
    results = []
    for f in files: 
        if f.endswith('.par'):
            results.append(f)
    print(results)
# Organize par files by time
# Make a regex to filter out time stamp in file name
    parbytime = re.compile(r'''(
        (\d{4})
        (\s|_|\.)
        (\d{2})
        (\s|_|\.)
        (\d{2})
        (\s|_|\.)
        (\d{2})
        (\s|_|\.)
        (\d{2})
        (\s|_|\.)
        (\d{2})
        )''', re.VERBOSE)
# Grab par files based on time stamps
    parresults = []
    for p in results:
        matched = parbytime.search(p)
        parresults.append(matched.group())
# Sort the par files by time stamp and extract the order
    print(parresults)
    l = np.argsort(parresults)
    print(l)
# Apply the order to the par files in memory
    res = np.array(results)
    newlist = res[l]
    print(newlist)
# Concatenate the par files and save the resultant dataframe
    for n in newlist:
        if newlist[0]:
            temp = pd.read_table(os.path.join(parpath,newlist[0]), header=None, names=['Trial Onset', 'Event Type','Stimulus Duration', 'Weight'], delim_whitespace=True)
        if newlist[1]:
            temp1 = pd.read_table(os.path.join(parpath,newlist[1]), header=None, names=['Trial Onset', 'Event Type','Stimulus Duration', 'Weight'], delim_whitespace=True)
        if newlist[2]:
            temp2 = pd.read_table(os.path.join(parpath,newlist[2]), header=None, names=['Trial Onset', 'Event Type','Stimulus Duration', 'Weight'], delim_whitespace=True)
        if newlist[3]:
            temp3 = pd.read_table(os.path.join(parpath,newlist[3]), header=None, names=['Trial Onset', 'Event Type','Stimulus Duration', 'Weight'], delim_whitespace=True)
        frames = [temp, temp1, temp2, temp3]
        concat = pd.concat(frames, sort=False, ignore_index=True)
        concat.to_csv(os.path.join(parpath,s + '_concatenated.csv'),index=False)
