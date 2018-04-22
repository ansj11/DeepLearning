# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
import threading
import time

#创建一个先进先出队列,制定最多两个元素,并指定整数类型
q = tf.FIFOQueue(2,"int32")
# 初始化队列元素
init = q.enqueue_many(([0,10],))

x = q.dequeue()

y = x+1

q_inc = q.enqueue([y])

with tf.Session() as sess:
    init.run()
    for i in range(5):
        v,_=sess.run([x,q_inc])
        print v


def MyLoop(coord,worker_id):
    while not coord.should_stop():
        if np.random.rand()<0.1:
            print "Stoping id %d\n" % worker_id
            coord.request_stop()
        else:
            print "Working on id: %d\n" % worker_id

        time.sleep(1)

coord = tf.train.Coordinator()
threads = [threading.Thread(target=MyLoop,args=(coord,i, )) for i in xrange(5)]

for t in threads: t.start()

coord.join(threads)