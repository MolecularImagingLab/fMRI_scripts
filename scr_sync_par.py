#!/usr/bin/env python
# coding: utf-8

# In[1]:


#! /home/lauri/anaconda3/bin/python

#load libraries
import os, sys 
import pandas as pd
import numpy as np
from nilearn import plotting
import matplotlib.pyplot as plt


# In[2]:


def readin():
# First argument is scr .txt file input, second argument is scr .txt file output
# Third argument is .par file input, fourth argument is .par file output
    input_scr = sys.argv[1]
    output_scr = sys.argv[2]
    input_par = sys.argv[3]
    output_par = sys.argv[4]
    return input_scr, output_scr, input_par, output_par


# In[1]:


def scr_mod(input_scr, output_scr):
#Reads in scr file and adds headers
    scr = pd.read_table(input_scr, header=0, names=['microsiemens', 'ch1', 'ch2', 'ch3'], delim_whitespace=True)
# Add time as a column, at a sampling rate of 200 Hz
    scr = scr.assign(time=[0 + (0.005)*i for i in range(len(scr))])[['time'] + scr.columns.tolist()]
# Start at iloc of 0 defines the time @ first electrical impulse - start1
# Every 11th float aftwerwards denotes an electrical impulse - starts
    start1 = (scr.loc[scr['ch2']==5, 'time'].iloc[0])
    starts = dict(scr.loc[scr['ch2']==5, 'time'].iloc[0::10])
# Startstop at iloc of 0 defines the time @ last electrical impulse of first run - end1
# Every 10th float afterwards denotes the starts and stops of the runs, except where there are test shocks
    startstops = dict(scr.loc[scr['ch1']==5, 'time'].iloc[0::10])
    liststartstop = []
# Removes values that are smaller than start1
    for l in list(startstops.values()):
        if l > start1:
            liststartstop.append(l)
# Test shocks register multiple times with proximate values
    npstartstop = np.array(liststartstop)
    startstoprounded = (npstartstop.round(decimals=0)).tolist()
# To remove test shocks, all rounded numbers repeated more than once discarded
    startstopunique = []
    for r in startstoprounded:
        x = startstoprounded.count(r)
        if x == 1:
            startstopunique.append(r)
# If all four runs of a session are accounted for, starts and stops are set below
    if len(startstopunique) == 7:
        print('starts and stops accounted for')
        end1 = startstopunique[0]
        start2 = startstopunique[1]
        end2 = startstopunique[2]
        start3 = startstopunique[3]
        end3 = startstopunique[4]
        start4 = startstopunique[5]
        end4 = startstopunique[6]
    if len(startstopunique) != 7:
        print('shifting index by 1')
        startstops = dict(scr.loc[scr['ch1']==5, 'time'].iloc[0::11])
        liststartstop = []
        for l in list(startstops.values()):
            if l > start1:
                liststartstop.append(l)
        npstartstop = np.array(liststartstop)
        startstoprounded = (npstartstop.round(decimals=0)).tolist()
        startstopunique = []
        for r in startstoprounded:
            x = startstoprounded.count(r)
            if x == 1:
                startstopunique.append(r)
            if len(startstopunique) == 7:
                print('starts and stops accounted for')
                end1 = startstopunique[0]
                start2 = startstopunique[1]
                end2 = startstopunique[2]
                start3 = startstopunique[3]
                end3 = startstopunique[4]
                start4 = startstopunique[5]
                end4 = startstopunique[6]
# Each impulse is sampled 10 times, the last 9 samples are discarded in channels 1 and 2 
    scr_ch1 = pd.DataFrame.from_dict(startstops, orient='index',columns=['ch1_cln'])
    scr_ch1.loc[(scr_ch1.ch1_cln > 0), 'ch1_cln'] = 5
    scr_ch2 = pd.DataFrame.from_dict(starts, orient='index',columns=['ch2_cln'])
    scr_ch2.loc[(scr_ch2.ch2_cln > 0), 'ch2_cln'] = 5
    merged = pd.concat([scr,scr_ch1,scr_ch2],axis=1)
    merged.fillna(0, inplace=True)
# Creates a new text file with clean channels 1 and 2
    merged.to_csv(output_scr)
    return start1, end1, start2, end2, start3, end3, start4, end4


# In[4]:


def par_mod(input_par, output_par, start1, end1, start2, end2, start3, end3, start4, end4):
# Must execute par_concat.py to successfully run this function
# Reads in .par file
    par = pd.read_csv(input_par)
# Calculates time to fill between runs
    fill1 = start2 - end1
    fill2 = start3 - end2
    fill3 = start4 - end3
# Run 1; index 0-69, Run 2; index 69-138, Run 3; index 138-207, Run 4; index 207-276
    onset = par['Trial Onset'].values
    synced_onset = np.add(onset, start1)
    run1 = list(synced_onset[0:69]) 
    run2 = list(synced_onset[69:138] + fill1 + 487.1)
    run3 = list(synced_onset[138:207] + fill1 + fill2 + 974.2)
    run4 = list(synced_onset[207:276] + fill1 + fill2 + fill3 + 1461)
    allruns = run1 + run2 + run3 + run4
# Replace old Trial Onsets with new Trial Onsets and save new par file
    par['Trial Onset'] = allruns
    par.to_csv(output_par, index=False, header = False, sep=' ')


# In[5]:


def main():
    input_scr, output_scr, input_par, output_par = readin()
    start1, end1, start2, end2, start3, end3, start4, end4 = scr_mod(input_scr, output_scr)
    par_mod(input_par, output_par, start1, end1, start2, end2, start3, end3, start4, end4)
    print('scr and par modifications complete')
if __name__ == "__main__":
    # execute only if run as a script
    main()

