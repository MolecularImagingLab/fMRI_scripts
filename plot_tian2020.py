#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Load Libraries
import os
import pandas as pd
import numpy as np
from nilearn import plotting, datasets, image
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import cm
import random


# In[44]:


# Creating custom colour palette based on Tian 2020.
# Generate 50 random colours
palette = []
for colour in range(0,50):
    palette.append("#{:06x}".format(random.randint(0, 0xFFFFFF)))
# Use matplotlib.colors.to_hex to get hex values
tian_lut = palette
tian_style = dict()
tian_style['tian_lut'] = colors.LinearSegmentedColormap.from_list(
    'tian_lut', tian_lut)
# Save colormaps in the scope of the module
locals().update(tian_style)
# Register cmaps in matplotlib too
for k, v in tian_style.items():
    cm.register_cmap(name=k, cmap=v)


# In[50]:


# Creates subcortical parcellation maps based on Tian 2020.
# Definition of datestamp as the current date 
date = pd.to_datetime('today').strftime("%d_%m_%Y_")
# Upload the atlas of choice. Tian 2020 dataset can be downloaded from https://github.com/yetianmed/subcortex
subctx_parc = image.load_img('/home/lauri/Downloads/Tian_Subcortex_S3_3T.nii')
# Define views and coordinates
views = {'z':'axial'}
coords = 3
# Create the image using the plot_roi function
for v in views:
    date_stamp = os.path.join('/home/lauri/Documents/temp/' + date + views[v] + '_tian2020.jpeg')
    tian_parc = plotting.plot_roi(subctx_parc, cut_coords=coords, colorbar = True, vmin = 1, vmax = 50, cmap = plt.cm.get_cmap('tian_lut',50), display_mode=v,black_bg=True)
    plt.savefig(date_stamp,dpi=600)

