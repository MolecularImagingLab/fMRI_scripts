#!/usr/bin/env python
# coding: utf-8

# In[2]:


#! /home/lauri/anaconda2/bin/python

import os, sys, shutil, re
import numpy as np

pwd=os.getcwd()
print('executing command in' + ' ' + pwd)


# In[6]:


def main():
    
    root = '/group/tuominen/EmoSal/subjects/'
    
    subject_id = sys.argv[1]
    par = 'par'
    filefolder = os.path.join(root, subject_id, par)
    print('This is the filefolder I defined ' + filefolder)
    results = list() 
    files = os.listdir(filefolder) # here I say ls and save output in files
    for f in files: 
        if f.endswith('.par'):
            results.append(f)    
    print(results)
         
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
    
    parresults = list()
    for p in results:
   
        matched = parbytime.search(p)
        parresults.append(matched.group())
     
    print(parresults)
    l = np.argsort(parresults)
    print(l)
    
    res = np.array(results)
    print(res[l])
    
    newlist = res[l]
    tfolder = '/group/tuominen/EmoSal/subjects'
    
    for i,r in enumerate(newlist):
        print(i)
        print(r)
        item = os.path.join(filefolder,r)
        print(item)
        run = str(i+1)
        target = os.path.join(tfolder, subject_id, 'bold', run.zfill(3), 'fc.par')
        print(target)
        
        shutil.copy(item,target)
    
    
if __name__ == "__main__":
    # execute only if run as a script
    main()

