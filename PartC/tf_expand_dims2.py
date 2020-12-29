import tensorflow as tf
import numpy as np

A2 = np.array([[[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [2, 4, 6, 8, 10]],
               [[1, 4, 3, 5, 7],
                [2, 4, 2, 3, 2],
                [9, 6, 9, 4, 7]]])  # 这种是3-D维度的张量。(2-3-5)

temp = tf.expand_dims(A2, 2)
shape2 = tf.shape(temp)
with tf.Session() as sess:
    print(sess.run(temp))
    print(sess.run(tf.shape(A2)))
    print(sess.run(tf.shape(temp)))
    print(sess.run(shape2))


"""

[[[[ 1  2  3  4  5]]

  [[ 6  7  8  9 10]]

  [[ 2  4  6  8 10]]]


 [[[ 1  4  3  5  7]]

  [[ 2  4  2  3  2]]

  [[ 9  6  9  4  7]]]]


[2 3 5]
[2 3 1 5]




"""


