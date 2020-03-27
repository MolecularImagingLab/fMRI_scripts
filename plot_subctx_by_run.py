#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[1]:


def pauli_atlas(views):
# Creates subcortical parcellation maps based on Pauli 2018
# Definiition of datestamp as the current date 
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
            if v== 'y':
                cut_coords=(-18,-8,-2,0,6,12,18)
                plotting.plot_prob_atlas(atlas, cut_coords=cut_coords, view_type='continuous', display_mode=v,black_bg=True, colorbar = True)
                plt.savefig(date_stamp,dpi=600)
            if v== 'z':
                cut_coords=(-12,-10,-6,-2,8,18,22)
                plotting.plot_prob_atlas(atlas, cut_coords=cut_coords, view_type='continuous', display_mode=v,black_bg=True, colorbar = True)
                plt.savefig(date_stamp,dpi=600)
            if v== 'x':
                cut_coords=(-32,-28,-24,-20,-16,-12,-8)
                plotting.plot_prob_atlas(atlas, cut_coords=cut_coords, view_type='continuous', display_mode=v,black_bg=True, colorbar = True)
                plt.savefig(date_stamp,dpi=600)


# In[8]:


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


# In[22]:


def choi_atlas(views):
# Creates subcortical parcellation maps based on Choi 2012
# Definiition of datestamp as the current date 
    date = pd.to_datetime('today').strftime("%d_%m_%Y_")
# Upload the atlas of choice. The Choi 2012 atlas is not included in nilearn datasets and must be uploaded manually
    striatal_parc = image.load_img('/usr/local/freesurfer/average/Choi_JNeurophysiol12_MNI152/Choi2012_7Networks_MNI152_FreeSurferConformed1mm_TightMask.nii.gz')
# Create the image using the plot_roi function
    for v in views:
        date_stamp = os.path.join('/home/lauri/Documents/temp/' + date + views[v] + '_choi2012.jpeg')
        if v== 'y':
            cut_coords=(-18,-8,-2,0,6,12,18)
            choi_parc = plotting.plot_roi(striatal_parc, cut_coords=cut_coords, colorbar = True, vmin = 1, vmax = 7, cmap = plt.cm.get_cmap('choi_lut',7), display_mode=v,black_bg=True)
            plt.savefig(date_stamp,dpi=600)
        if v== 'z':
            cut_coords=(-12,-10,-6,-2,8,18,22)
            choi_parc = plotting.plot_roi(striatal_parc, cut_coords=cut_coords, colorbar = True, cmap = plt.cm.get_cmap('choi_lut',7), display_mode=v,black_bg=True)
            plt.savefig(date_stamp,dpi=600)
        if v== 'x':
            cut_coords=(-32,-28,-24,-20,-16,-12,-8)
            choi_parc = plotting.plot_roi(striatal_parc, cut_coords=cut_coords, colorbar = True, cmap = plt.cm.get_cmap('choi_lut',7), display_mode=v,black_bg=True)
            plt.savefig(date_stamp,dpi=600)


# In[21]:


def stat_maps(views):
# Creates statistical maps of subcortical structures in saggital, coronal and axial views
# State path to statistical mask files generated by freesurfer processes
    path = "/home/lauri/Documents/temp/"
    statpath = os.listdir(path)
    statfile = []
# Creates a function to grab all subcortical statistical files 
    for s in statpath:
        if s.startswith('mni') and s.endswith('gz'):
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
            if v== 'y':
                cut_coords=(-18,-8,-2,0,6,12,18)
                stat_map = plotting.plot_stat_map(os.path.join(path,f), threshold = 1.3, vmax = 5, cut_coords=cut_coords, display_mode=v,black_bg=True)
                plt.savefig(date_stamp,dpi=600)
            if v== 'z':
                cut_coords=(-12,-10,-6,-2,8,18,22)
                stat_map = plotting.plot_stat_map(os.path.join(path,f), threshold = 1.3, vmax = 5, cut_coords=cut_coords, display_mode=v,black_bg=True)
                plt.savefig(date_stamp,dpi=600)
            if v== 'x':
                cut_coords=(-32,-28,-24,-20,-16,-12,-8)
                stat_map = plotting.plot_stat_map(os.path.join(path,f), threshold = 1.3, vmax = 5, cut_coords=cut_coords, display_mode=v,black_bg=True)
                plt.savefig(date_stamp,dpi=600)


# In[8]:


def atlas_views(input_atlas, views):
    if input_atlas == 'pauli':
        pauli_atlas(views)
        print('generating pauli 2018 atlas overlay')
    if input_atlas == 'choi':
        choi_cmaps()
        choi_atlas(views)
        print('generating choi 2012 atlas overlay')
    else:
        print('no atlas was chosen and no atlas images will be generated')


# In[7]:


def brain_views(input_views):
    if str(input_views) == ('x'):
        views = {'x':'saggital'}
        print('generating brain images in saggital view only')
    if str(input_views) == ('y'):
        views = {'y':'coronal'}
        print('generating brain images in coronal view only')
    if str(input_views) == ('z'):
        views = {'z':'axial'}
        print('generating brain images in axial view only')
    if str(input_views) == ('xy') or ('yx'):
        views = {'x':'saggital','y':'coronal'}
        print('generating brain images in saggital and coronal views')
    if str(input_views) == ('yz') or ('zy'):
        views = {'y':'coronal','z':'axial'}
        print('generating brain images in coronal and axial views')
    if str(input_views) == ('xz') or ('zx'):
        views = {'x':'saggital','z':'axial'}
        print('generating brain images in saggital and axial views')
    if str(input_views) == ('xyz') or ('xzy') or ('zyx') or ('zxy') or ('yzx') or ('yxz'):
        views = {'x':'saggital','y':'coronal','z':'axial'}
        print('generating brain images in all slice views')
    else:
        print('please input brain view display as x for saggital, y for coronal or z for axial')
    return views


# In[ ]:


def inputs_please():
    input_views = sys.argv[1]
    input_atlas = sys.argv[2]
    return input_views, input_atlas


# In[ ]:


def main():
    input_views, input_atlas = inputs_please()
    views = brain_views(input_views)
    atlas_views(input_atlas, views)
    stat_maps(views)
    print('statistical image generation complete')
if __name__ == "__main__":
    # execute only if run as a script
    main()


# In[11]:


'yz' == 'xyz'


# In[ ]:



