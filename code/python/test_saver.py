import tensorflow as tf

v1 = tf.Variable(tf.constant(1.0,shape=[1]),name='v1')
v2 = tf.Variable(tf.constant(2.0,shape=[1]),name='v2')

result = v1 + v2

init = tf.global_variables_initializer()

saver = tf.train.Saver()

with tf.Session() as sess:

    sess.run(init)
    print sess.run(result)
    saver.save(sess,"./models/model.ckpt")

x = tf.placeholder(tf.float32,shape=[1],name='x_input')

w = tf.Variable(tf.constant(2.0,shape=[1]),name='weights')
b = tf.Variable(tf.constant(1.0,shape=[1]),name='bias')

result = tf.nn.relu(tf.multiply(x,w) + b)

saver = tf.train.Saver()

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    saver.save(sess,"./models/model1.ckpt")