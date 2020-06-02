#!/usr/bin/env python
# coding: utf-8

# In[2]:


#! /home/lauri/anaconda3/bin/python

#load libraries
import os, sys 
import pandas as pd
import numpy as np
from nilearn import plotting
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math
import seaborn as sns


# In[108]:


# Define file path
datapath = '/media/lauri/My Passport/My_Computer/Documents/sync_me/EmoSal/reports/19_05_2020_/19_05_2020_tziortzi2014_analysis_byrun.csv'
# Read-in data
rois = pd.read_csv(datapath)
status = rois['Status']
# Average the data by Status
#avg = rois.groupby('Status').agg(np.mean)
# Limbic Network Data
limbic_1 = rois['Limbic_Network_csp_pr001'] - rois['Limbic_Network_csm_pr001']
limbic_2 = rois['Limbic_Network_csp_pr002'] - rois['Limbic_Network_csm_pr002']
limbic_3 = rois['Limbic_Network_csp_pr003'] - rois['Limbic_Network_csm_pr003']
limbic_4 = rois['Limbic_Network_csp_pr004'] - rois['Limbic_Network_csm_pr004']
frames = [status, limbic_1, limbic_2, limbic_3, limbic_4]
limbic = pd.concat(frames, axis=1)
limbic.columns = ['Status','Run 1', 'Run 2', 'Run 3', "Run 4"]
# Executive Network Data
exec_1 = rois['Executive_Network_csp_pr001'] - rois['Executive_Network_csm_pr001']
exec_2 = rois['Executive_Network_csp_pr002'] - rois['Executive_Network_csm_pr002']
exec_3 = rois['Executive_Network_csp_pr003'] - rois['Executive_Network_csm_pr003']
exec_4 = rois['Executive_Network_csp_pr004'] - rois['Executive_Network_csm_pr004']
frames = [status, exec_1, exec_2, exec_3, exec_4]
executive = pd.concat(frames, axis=1)
executive.columns = ['Status','Run 1', 'Run 2', 'Run 3', "Run 4"]
# Motor Network Data
motor_1 = rois['Motor_Network_csp_pr001'] - rois['Motor_Network_csm_pr001']
motor_2 = rois['Motor_Network_csp_pr002'] - rois['Motor_Network_csm_pr002']
motor_3 = rois['Motor_Network_csp_pr003'] - rois['Motor_Network_csm_pr003']
motor_4 = rois['Motor_Network_csp_pr004'] - rois['Motor_Network_csm_pr004']
frames = [status, motor_1, motor_2, motor_3, motor_4]
motor = pd.concat(frames, axis=1)
motor.columns = ['Status','Run 1', 'Run 2', 'Run 3', "Run 4"]


# In[114]:


# Plot Results (by run)
networks = [limbic, executive, motor]
networks_names = ['Limbic','Executive','Motor']
for n,l in zip(networks,networks_names):
    m = pd.melt(n, id_vars =['Status'], value_vars =['Run 1', 'Run 2','Run 3','Run 4'], var_name='Session',value_name='%change')
    sns.set_style('dark')
    sns.set_palette('Dark2')
    alldata = (sns.barplot(x='Session', y='%change', hue='Status', data=m,linewidth=2.5, capsize=0.2, edgecolor='black').set_title(os.path.join(l + ' - CS+ versus CS-'))).get_figure()
    plt.xlabel('Sessions')
    plt.ylabel('% Change (fMRI activity)')
    alldata.savefig(os.path.join('/home/lauri/Documents/temp/',l+'fmri_contrast_byrun.jpg'), dpi=300)
    plt.clf()


# In[115]:


# Plot Results (all 4 runs together)
networks = [limbic, executive, motor]
networks_names = ['Limbic','Executive','Motor']
for n,l in zip(networks,networks_names):
    m = pd.melt(n, id_vars =['Status'], value_vars =['Run 1', 'Run 2','Run 3','Run 4'], var_name='Session',value_name='%change')
    sns.set_style('dark')
    sns.set_palette('Dark2')
    alldata = (sns.barplot(x='Status', y='%change', hue='Status', data=m,linewidth=2.5, capsize=0.2, edgecolor='black').set_title(os.path.join(l + ' - CS+ versus CS-'))).get_figure()
    plt.xlabel('Condition')
    plt.ylabel('% Change (fMRI activity)')
    alldata.savefig(os.path.join('/home/lauri/Documents/temp/',l+'fmri_contrast_allruns.jpg'), dpi=300)
    plt.clf()

