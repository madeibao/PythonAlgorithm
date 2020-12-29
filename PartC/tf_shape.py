
import tensorflow as tf
import numpy as np

 

A = np.array([[[1, 1, 1],
               [2, 2, 2]],
              [[3, 3, 3],
               [4, 4, 4]],
              [[5, 5, 5],
               [6, 6, 6]]])
t = tf.shape(A)

with tf.Session() as sess:
    print(sess.run(t))


# 输出为[3,2,3]