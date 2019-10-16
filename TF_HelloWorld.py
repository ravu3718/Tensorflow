# TensorFlow Hello World Program

import tensorflow as tf
c = tf.constant('Hello, world!')
with tf.Session() as sess:
    print sess.run(c)