#!/usr/bin/env python
# coding: utf-8

# In[14]:


#! /home/lauri/anaconda3/bin/python
# Load libraries
import os, sys, glob, re
import nibabel as nb
import pandas as pd
import numpy as np
from nilearn import plotting
from nilearn import datasets
from nilearn import image
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import cm


# In[29]:


def pauli_atlas(views, coords):
# Creates subcortical parcellation maps based on Pauli 2018
# Definition of datestamp as the current date 
    date = pd.to_datetime('today').strftime("%d_%m_%Y_")
# Upload the atlas of choice, for other atlases see documentation 8.2.11: Visualizing 4D probabilistic atlas maps
    subcortex = datasets.fetch_atlas_pauli_2017()
    atlas_types = {
                   'Pauli2018 Subcortical Atlas': subcortex.maps,
                   }
# Create the image using the plot_prob_atlas function
    for name, atlas in sorted(atlas_types.items()):
        for v in views:
            date_stamp = os.path.join('/home/lauri/Documents/temp/' + date + views[v] + '_pauli2018.jpeg')
            cut_coords=coords
            plotting.plot_prob_atlas(atlas, cut_coords=cut_coords, view_type='continuous', display_mode=v,black_bg=True, colorbar = True)
            plt.savefig(date_stamp,dpi=600)


# In[30]:


def yeo2015_atlas(views, coords):
# Creates task-based parcellation maps based on Yeo 2015
# Definition of datestamp as the current date 
    date = pd.to_datetime('today').strftime("%d_%m_%Y_")
# Upload the atlas of choice. The Yeo 2015 atlas is not included in nilearn datasets and must be uploaded manually
    task_parc = image.load_img('/usr/local/freesurfer/average/Yeo_Brainmap_MNI152/Yeo_12Comp_PrActGivenComp_FSL_MNI152_2mm.nii.gz')
# Create the image using the plot_prob_atlas function
    for v in views:
        date_stamp = os.path.join('/home/lauri/Documents/temp/' + date + views[v] + '_yeo2015.jpeg')
        cut_coords=coords
        choi_parc = plotting.plot_prob_atlas(task_parc, cut_coords=cut_coords, colorbar = True, vmin = 1, vmax = 12, cmap = plt.cm.get_cmap('tab20b',12), view_type='filled_contours', display_mode=v,black_bg=True)
        plt.savefig(date_stamp,dpi=600)


# In[31]:


def choi_cmaps():
# Creating custom colour palette based on Choi 2012
# Colours in order: Purple, Blue, Green, Violet, Cream, Orange, Red
# These are the RGB values defined in the colorLUT.txt  
    choi_col = np.array([(120, 18, 134), (70, 130, 180),
                            (0, 118, 14), (196, 58, 250),
                            (220, 248, 164), (230, 148, 34),
                            (205, 62, 78)]) / 255
# Use matplotlib.colors.to_hex to get hex values
    choi_lut = ['#800080', '#0000ff', '#008000', '#ee82ee',
               '#eee8aa', '#ffa500','#ff0000']

    choi_style = dict()

    choi_style['choi_col'] = colors.LinearSegmentedColormap.from_list(
        'choi_col', choi_col.tolist())
    choi_style['choi_lut'] = colors.LinearSegmentedColormap.from_list(
        'choi_lut', choi_lut)

# Save colormaps in the scope of the module
    locals().update(choi_style)
# Register cmaps in matplotlib too
    for k, v in choi_style.items():
        cm.register_cmap(name=k, cmap=v)
# To confirm cmap is registered view list of colormaps using matplotlib.pyplot.colormaps


# In[33]:


def choi_atlas(views, coords):
# Creates subcortical parcellation maps based on Choi 2012
# Definition of datestamp as the current date 
    date = pd.to_datetime('today').strftime("%d_%m_%Y_")
# Upload the atlas of choice. The Choi 2012 atlas is not included in nilearn datasets and must be uploaded manually
    striatal_parc = image.load_img('/usr/local/freesurfer/average/Choi_JNeurophysiol12_MNI152/Choi2012_7Networks_MNI152_FreeSurferConformed1mm_TightMask.nii.gz')
# Create the image using the plot_roi function
    for v in views:
        date_stamp = os.path.join('/home/lauri/Documents/temp/' + date + views[v] + '_choi2012.jpeg')
        cut_coords=coords
        choi_parc = plotting.plot_roi(striatal_parc, cut_coords=cut_coords, colorbar = True, vmin = 1, vmax = 7, cmap = plt.cm.get_cmap('choi_lut',7), display_mode=v,black_bg=True)
        plt.savefig(date_stamp,dpi=600)


# In[34]:


def tziortzi_cmaps():
# Creating custom colour palette based on Tziortzi 2014
# Colours in order: Red (Limibic), Yellow (Executive), Green (Motor)
# These are the RGB values defined in the colorLUT.txt  
    tziortzi_col = np.array([(241, 14, 14), (255, 222, 82),
                        (107, 196, 86)]) / 255
# Use matplotlib.colors.to_hex to get hex values
    tziortzi_lut = ['#F10E0E', '#FFDE52', '#6BC456']

    tziortzi_style = dict()

    tziortzi_style['tziortzi_col'] = colors.LinearSegmentedColormap.from_list(
        'tziortzi_col', tziortzi_col.tolist())
    tziortzi_style['tziortzi_lut'] = colors.LinearSegmentedColormap.from_list(
        'tziortzi_lut', tziortzi_lut)
# Save colormaps in the scope of the module
    locals().update(tziortzi_style)
# Register cmaps in matplotlib too
    for k, v in tziortzi_style.items():
        cm.register_cmap(name=k, cmap=v)
# To confirm cmap is registered view list of colormaps using matplotlib.pyplot.colormaps


# In[36]:


def tziortzi_atlas(views, coords):
# Creates task-based parcellation maps based on Tziortzi 2014
# Definition of datestamp as the current date 
    date = pd.to_datetime('today').strftime("%d_%m_%Y_")
# Upload the atlas of choice. The Tziortzi 2014 atlas is not included in nilearn datasets and must be uploaded manually
    striatal_parc = image.load_img('/usr/local/fsl/data/atlases/Striatum/striatum-con-label-thr50-3sub-2mm.nii.gz')
# Create the image using the plot_prob_atlas function
    for v in views:
        date_stamp = os.path.join('/home/lauri/Documents/temp/' + date + views[v] + '_Tziortzi2014.jpeg')
        cut_coords=coords
        tziortzi_parc = plotting.plot_roi(striatal_parc, cut_coords=cut_coords, colorbar = True, vmin = 1, vmax = 3, cmap = plt.cm.get_cmap('tziortzi_lut',3), display_mode=v,black_bg=True)
        plt.savefig(date_stamp,dpi=600)


# In[58]:


def stat_maps(views, coords):
# Creates statistical maps of subcortical structures in saggital, coronal and axial views
# State path to statistical mask files generated by freesurfer processes
    path = "/home/lauri/Documents/FearCond_Copy/subjects/"
    statpath = os.listdir(path)
    statfile = []
# Creates a function to grab all subcortical statistical files 
    for s in statpath:
        if s.startswith('psychosis') and s.endswith('pos05.nii'):
            statfile.append(s)
    print('Making images for:')
    statfile.sort()
    print(statfile)
# Definiition of datestamp as the current date
    date = pd.to_datetime('today').strftime("%d_%m_%Y_")
# Create the image using the plot_stat_map function
    for f in statfile:
        for v in views:
            date_stamp = os.path.join('/home/lauri/Documents/temp/' + date + views[v] + f + '.jpeg')
            cut_coords=[int(c) for c in coords]
            stat_map = plotting.plot_stat_map(os.path.join(path,f), threshold = 1.3, vmax = 5, cut_coords=cut_coords, display_mode=v,black_bg=True)
            plt.savefig(date_stamp,dpi=600)


# In[59]:


def atlas_views(input_atlas, views):
    if input_atlas == 'pauli2018':
        pauli_atlas(views, coords)
        print('generating pauli 2018 atlas overlay')
    elif input_atlas == 'yeo2015':
        yeo2015_atlas(views, coords)
        print('generating yeo 2015 atlas overlay')    
    elif input_atlas == 'choi2012':
        choi_cmaps()
        choi_atlas(views, coords)
        print('generating choi 2012 atlas overlay')
    elif input_atlas == 'tziortzi2014':
        tziortzi_cmaps()
        tziortzi_atlas(views, coords)
        print('generating tziortzi 2014 atlas overlay')
    else:
        print('no atlas was chosen and no atlas images will be generated.')
        print('atlas options: pauli2018, yeo2015, choi2012, tziortzi2014.')


# In[66]:


def brain_views(input_views):
    if str(input_views) == ('x'):
        views = {'x':'saggital'}
        coords = input("Enter saggital coordinates.")
        coords = coords.split(',')
        print('generating brain images in saggital view only.')
    elif str(input_views) == ('y'):
        views = {'y':'coronal'}
        coords = input("Enter coronal coordinates.")
        coords = coords.split(',')
        print('generating brain images in coronal view only.')
    elif str(input_views) == ('z'):
        views = {'z':'axial'}
        coords = input("Enter axial coordinates.")
        coords = coords.split(',')
        print('generating brain images in axial view only.')
    elif str(input_views) == ('all'):
        views = {'x':'saggital','y':'coronal','z':'axial'}
        coords = input("Enter coordinates for all views.")
        coords = coords.split(',')
        print('generating brain images in all slice views.')
    else:
        print('Please input brain view display as x for saggital, y for coronal, z for axial or all for all.')
    return views, coords


# In[67]:


def inputs_please():
    input_views = input("Please input brain view display as x for saggital, y for coronal, z for axial or all for all.")
    input_atlas = input("Please input brain atlas as pauli2018, yeo2015, choi2012, tziortzi2014 or none.")
    return input_views, input_atlas


# In[69]:


def main():
    input_views, input_atlas = inputs_please()
    views, coords = brain_views(input_views)
    atlas_views(input_atlas, views)
    stat_maps(views, coords)
    print('statistical image generation complete')
if __name__ == "__main__":
    # execute only if run as a script
    main()

