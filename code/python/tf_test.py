# -*- coding: utf-8 -*-

import tensorflow as tf
import os
import numpy as np
import cv2
from IPython import embed

img = cv2.imread('0.jpg', 0)

img = img.reshape(1,400,640,1)

x = tf.placeholder('float32', shape=[1,400,640,1], name='input')

init = np.array([1,-2,1,-2,4,-2,1,-2,1]).reshape(3,3,1,1).astype('float32')

w = tf.Variable(initial_value=init)

conv1 = tf.nn.conv2d(x,w,strides=[1,1,1,1],padding='SAME',name='conv')

y = tf.layers.conv2d_transpose(conv1,1,3,strides=1,kernel_initializer=tf.constant_initializer(init),name='deconv',padding='SAME')

# loss = tf.reduce_mean(tf.abs(x-y))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    conv,deconv = sess.run([conv1,y], feed_dict={x:img})
    print(conv.shape,deconv.shape)
    #print('The construct loss is %d' % l[0])

embed()


