#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 12:35:52 2017

@author: jian
"""


import os
path1 = '/home/jian/Downloads/tf_unet/train/'
path2 = '/home/jian/Downloads/tf_unet/1st_manual/'
file1 = os.listdir(path1)
file2 = os.listdir(path2)

#for i in range(len(file1)):
#    os.rename(file1,path1+os.path.splitext(file1[i])[0]+".tif")
#for i in range(len(file2)):
#    os.rename(file2[i],path2+os.path.splitext(file2[i])[0]+'_mask.tif')
    
for i in range(len(file1)):
    os.rename(file1,path1+str(i+1)+".tif")
for i in range(len(file2)):
    os.rename(file2[i],path2+str(i+1)+'_mask.tif')