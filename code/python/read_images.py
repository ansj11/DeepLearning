#-*- coding: utf-8 -*-
#====================================================
#
#   This file read images file and draw the hist image
#
#====================================================

import os
import h5py
import numpy as np
from PIL import Image

def write_hdf5(arr,outfile):
    with h5py.File(outfile,'w') as f:
        f.create_dataset("image",data=arr,dtype=arr.dtype)


imgs_dir = '/media/ansj/LENOVO/MLCode/dataSet/database/测试集各种病灶RGB图像(436-422)(99)/'
labels_dir = '/media/ansj/LENOVO/MLCode/dataSet/database/测试集各种病灶groundtruth(436-422)二值化(99)/'

save_path = '/home/ansj/dataSet/'

N = 99
channels = 3
height = 422
width = 436

def get_datasets(imgs_dir,labels_dir):
    imgs = np.empty((N,height,width,channels))
    labels = np.empty((N,height,width,channels))
    for path,subdirs,files in os.walk(imgs_dir):
        for path2, subdirs2, files2 in os.walk(labels_dir):
            for i in range(len(files)):
                print "original image: "+files[i]
                img = Image.open(imgs_dir+files[i])
                imgs[i] = np.asarray(img)
                label_name = files2[i]
                print "ground truth: " + label_name
                label = Image.open(labels_dir+label_name)
                labels[i] = np.asarray(label)

    print "imgs max: " + str(np.max(imgs))
    print "imgs min: " + str(np.min(imgs))
    labels = labels[:,:,:,0]/255.0
    print "labels max: " + str(np.max(labels))
    print "labels min: " + str(np.min(labels))
    assert(np.max(labels)==1 and np.min(labels)==0)
    print "ground truth are correctly within pixel value range 0-255 (black-white)"

    imgs = np.transpose(imgs,(0,3,1,2))
    assert(imgs.shape == (N,channels,height,width))
    labels = np.reshape(labels,(N,1,height,width))
    print imgs.shape,labels.shape
    return imgs, labels

imgs_train, labels_train = get_datasets(imgs_dir,labels_dir)

#hist(x, bins=None, range=None, normed=False, weights=None, cumulative=False, bottom=None, histtype=u'bar', align=u'mid', orientation=u'vertical', rwidth=None, log=False, color=None, label=None, stacked=False, hold=None, data=None, **kwargs)
'''
from pylab import *
figure()
hist((imgs_train[:,0,:,:]*(1-labels_train[:,0,:,:])).flatten(),255,(1,255),normed=True,color='green', alpha=0.75)
hist((imgs_train[:,0,:,:]*labels_train[:,0,:,:]).flatten(),255,(1,255),normed=True,color='red', alpha=0.75)
xlabel('grayscale')
ylabel('probability')
#添加标题
title('Histogram of retinal image')
#添加文字
#text(60, .025, r'$\mu=100,\ \sigma=15$')
#axis([1, 254, 0, 0.03])
grid(True)
show()

figure()
hist((imgs_train[:,1,:,:]*(1-labels_train[:,0,:,:])).flatten(),255,(1,255),normed=True,color='green',alpha=0.75)
hist((imgs_train[:,1,:,:]*labels_train[:,0,:,:]).flatten(),255,(1,255),normed=True,color='red',alpha=0.75)
xlabel('grayscale')
ylabel('probability')
#axis([1, 254, 0, 0.03])
#添加标题
title('Histogram of retinal image')
grid(True)
show()

figure()
hist((imgs_train[:,2,:,:]*(1-labels_train[:,0,:,:])).flatten(),255,(1,255),normed=True,color='green',alpha=0.75)
hist((imgs_train[:,2,:,:]*labels_train[:,0,:,:]).flatten(),255,(1,255),normed=True,color='red',alpha=0.75)
xlabel('grayscale')
ylabel('probability')
#axis([1, 250, 0, 0.03])
#添加标题
title('Histogram of retinal image')
grid(True)
show()
'''

print "saving train datasets"
write_hdf5(imgs_train, save_path + "images99.hdf5")
write_hdf5(labels_train, save_path + "labels99.hdf5")



