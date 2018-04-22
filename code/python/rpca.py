import tensorflow as tf
import numpy as np
import h5py

batch_size = 151
height = 422
width  = 436
learning_rate = 0.001
STEPS = 100
dataset_size = 151

path = '/home/ansj/dataSet/imdb151.mat'
f = h5py.File(path)
X = f['images'][:,0,:,:]
Y = f['labels'][:,0,:,:]

x = tf.placeholder(tf.float32,shape=(None,height*width),name='images')
y = tf.placeholder(tf.float32,shape=(None,height*width),name='labels')

W = tf.Variable(tf.random_normal(shape=[height*width,100],dtype=tf.float32))
D = tf.Variable(tf.random_normal(shape=[100,height*width],dtype=tf.float32))

s1 = tf.matmul(x,W)
o1 = x-tf.matmul(s1,D)
o2 = tf.nn.relu(o1)

s2 = tf.matmul(x,W)-tf.matmul(o2,W)
o3 = x-tf.matmul(s2,D)
o4 = tf.nn.relu(o3)

s2 = tf.matmul(x,W)-tf.matmul(o2,W)
o3 = x-tf.matmul(s2,D)
o4 = tf.nn.relu(o3)

loss = tf.reduce_mean(tf.square(o4-y))
train_op = tf.train.GradientDescentOptimizer(1e-10).minimize(loss)
saver = tf.train.Saver()

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    for i in range(STEPS):
        start = i*batch_size % dataset_size
        end = min(start+batch_size,dataset_size)

        images = np.reshape(X[start:end],[len(X[start:end]),height*width])
        labels = np.reshape(Y[start:end],[len(X[start:end]),height*width])
        _,l = sess.run([train_op,loss],feed_dict={x:images,y:labels})
        if i%10 == 0:
            print "Epoch:{}, loss:{}.".format(i,l)
            saver.save(sess,'./models/rpca.ckpt')