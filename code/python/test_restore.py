#-*- coding: utf-8 -*-

import tensorflow as tf

v1 = tf.Variable(tf.constant(1.0,shape=[1]),name='v1')
v2 = tf.Variable(tf.constant(2.0,shape=[1]),name='v2')

result = v1 + v2

saver = tf.train.Saver()

with tf.Session() as sess:
    saver.restore(sess,"./models/model.ckpt")
    print sess.run(result)


saver = tf.train.import_meta_graph("./models/model.ckpt.meta")

with tf.Session() as sess:
    saver.restore(sess,"./models/model.ckpt")
    print sess.run(tf.get_default_graph().get_tensor_by_name("add:0"))
    # 每个节点默认会有一个名称,可作为输出变量的名称
x = tf.placeholder(tf.float32,shape=[1])
saver = tf.train.import_meta_graph("./models/model1.ckpt.meta")

with tf.Session() as sess:
    saver.restore(sess,"./models/model1.ckpt")
    print sess.run(tf.get_default_graph().get_tensor_by_name("add:0"),feed_dict={x:})