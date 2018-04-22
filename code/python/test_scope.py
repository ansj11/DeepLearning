import tensorflow as tf

with tf.variable_scope("foo"):
    v = tf.get_variable("v",[1],initializer=tf.constant_initializer(1.0))

#with tf.variable_scope("foo"):
#    v = tf.get_variable("v",[1])

with tf.variable_scope("foo",reuse=True):
    v1 = tf.get_variable("v",[1])
    print v==v1

#with tf.variable_scope("bar",reuse=True):
#    v = tf.get_variable("v",[1])

with tf.variable_scope("root"):
    print tf.get_variable_scope().reuse
    with tf.variable_scope("foo",reuse=True):
        print tf.get_variable_scope().reuse
        with tf.variable_scope("bar"):
            print tf.get_variable_scope().reuse
    print tf.get_variable_scope().reuse