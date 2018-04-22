import tensorflow as tf

a = tf.constant([1.0,2.0,3.0],name='input1')
b = tf.Variable(tf.random_uniform([3]),name='input2')
c = tf.add_n([a,b],name='add')
sess = tf.Session()
sess.run(tf.global_variables_initializer())
writer = tf.train.SummaryWriter('./log',sess.graph)
writer.close()


