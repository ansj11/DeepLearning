
import tensorflow as tf

hello_op = tf.constant('hello, tf~!')
a = tf.constant(10)
b = tf.constant(32)
op = tf.subtract(b,a)

with tf.Session() as sess:
    print(sess.run(hello_op))
    print(sess.run(op))
