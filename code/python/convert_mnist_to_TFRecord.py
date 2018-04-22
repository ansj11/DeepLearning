# -*- coding: utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np

# 生成整数型属性
def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

# 生成字符串型属性
def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

mnist = input_data.read_data_sets('./mnist',dtype=tf.uint8,one_hot=True)

images = mnist.train.images
labels = mnist.train.labels

pixels = images.shape[1] # 每张图片的像素总数
num_examples = mnist.train.num_examples # mnist 自带key

filename = './dataset.tfrecord'

with tf.python_io.TFRecordWriter(filename) as f:
    for i in range(num_examples):
        image_raw = images[i].tostring()
        example = tf.train.Example(features=tf.train.Features(feature={
            'pixels': _int64_feature(pixels),
            'label': _int64_feature(np.argmax(labels[i])),
            'image_raw': _bytes_feature(image_raw)
        }))
        f.write(example.SerializeToString())
    print("TFRecord have been saved")

# 加载TFRecord程序

reader =  tf.TFRecordReader()
filename_queue = tf.train.string_input_producer([filename])
# 连载的读取一个样例,也可以用reader_up_to读入多个样例
_,serialized_example = reader.read(filename_queue)
# 解析读入的一个样例,也可以用parse_example解析多个样例
features = tf.parse_single_example(
    serialized_example,
    features = {
        'image_raw': tf.FixedLenFeature([],tf.string),
        'pixels': tf.FixedLenFeature([],tf.int64),
        'label': tf.FixedLenFeature([],tf.int64)
    }
)
# tf.decode_raw将字符串解析成数组
images = tf.decode_raw(features['image_raw'],tf.uint8)
labels = tf.cast(features['label'],tf.int32)
pixels = tf.cast(features['pixels'],tf.int32)

with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess,coord=coord)
    for i in range(num_examples):
        image, label, pixel = sess.run([images,labels, pixels])
        print image.shape,label.shape,pixel.shape