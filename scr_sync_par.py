#!/usr/bin/env python
#! /home/lauri/anaconda3/bin/python
#load libraries
import os, sys 
import pandas as pd
import numpy as np
from nilearn import plotting
import matplotlib.pyplot as plt

def readin():
# First argument is scr .txt file input, second argument is scr .txt file output
# Third argument is .par file input, fourth argument is .par file output
    input_scr = sys.argv[1]
    output_scr = sys.argv[2]
    input_par = sys.argv[3]
    output_par = sys.argv[4]
    return input_scr, output_scr, input_par, output_par

def scr_mod(input_scr, output_scr):
#Reads in scr file and adds headers
    scr = pd.read_table(input_scr, header=0, names=['microsiemens', 'ch1', 'ch2', 'ch3'], delim_whitespace=True)
# Add time as a column, at a sampling rate of 200 Hz
    scr = scr.assign(time=[0 + (0.005)*i for i in range(len(scr))])[['time'] + scr.columns.tolist()]
# Start at iloc of 0 defines the time @ first electrical impulse
# Every 11th float aftwerwards denotes an electrical impulse
    start = (scr.loc[scr['ch2']==5, 'time'].iloc[0])
    start1 = dict(scr.loc[scr['ch2']==5, 'time'].iloc[0::11])
# Startstop at iloc of 0 defines the time @ last electrical impulse of first run
# Every 11th float afterwards denotes the starts and stops of the runs
    startstop = dict(scr.loc[scr['ch1']==5, 'time'].iloc[0::11])
    stop = (scr.loc[scr['ch1']==5, 'time'].iloc[0])
    start2 = (scr.loc[scr['ch1']==5, 'time'].iloc[11])
    end2 = (scr.loc[scr['ch1']==5, 'time'].iloc[22])
    start3 = (scr.loc[scr['ch1']==5, 'time'].iloc[33])
    end3 = (scr.loc[scr['ch1']==5, 'time'].iloc[44])
    start4 = (scr.loc[scr['ch1']==5, 'time'].iloc[55])
    end4 = (scr.loc[scr['ch1']==5, 'time'].iloc[66])
# Each impulse is sampled 11 times, the last 10 samples are discarded in channels 1 and 2 
    scr_ch1 = pd.DataFrame.from_dict(startstop, orient='index',columns=['ch1_cln'])
    scr_ch1.loc[(scr_ch1.ch1_cln > 0), 'ch1_cln'] = 5
    scr_ch2 = pd.DataFrame.from_dict(start1, orient='index',columns=['ch2_cln'])
    scr_ch2.loc[(scr_ch2.ch2_cln > 0), 'ch2_cln'] = 5
    merged = pd.concat([scr,scr_ch1,scr_ch2],axis=1)
    merged.fillna(0, inplace=True)
# Creates a new text file with clean channels 1 and 2
    merged.to_csv(output_scr)
    return start, stop, start2, end2, start3, end3, start4, end4

def par_mod(input_par, output_par, start, stop, start2, end2, start3, end3, start4, end4):
# Must execute par_concat.py to successfully run this function
# Reads in .par file
    par = pd.read_csv(input_par)
# Calculates time to fill between runs
    fill1 = start2 - stop
    fill2 = start3 - end2
    fill3 = start4 - end3
# Run 1; index 0-69, Run 2; index 69-138, Run 3; index 138-207, Run 4; index 207-276
    onset = par['Trial Onset'].values
    synced_onset = np.add(onset, start)
    run1 = list(synced_onset[0:69]) 
    run2 = list(synced_onset[69:138] + fill1 + 487.1)
    run3 = list(synced_onset[138:207] + fill1 + fill2 + 974.2)
    run4 = list(synced_onset[207:276] + fill1 + fill2 + fill3 + 1461.3)
    allruns = run1 + run2 + run3 + run4
# Replace old Trial Onsets with new Trial Onsets and save new par file
    par['Trial Onset'] = allruns
    par.to_csv(output_par, index=False, header = False, sep=' ')

def main():
    input_scr, output_scr, input_par, output_par = readin()
    start, stop, start2, end2, start3, end3, start4, end4 = scr_mod(input_scr, output_scr)
    par_mod(input_par, output_par, start, stop, start2, end2, start3, end3, start4, end4)
    print('scr and par modifications complete')
if __name__ == "__main__":
    # execute only if run as a script
    main()

