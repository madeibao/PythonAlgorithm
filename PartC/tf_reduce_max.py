import tensorflow as tf
import numpy as np

a = np.array([[1, 2],
              [5, 3],
              [2, 6]])

b = tf.Variable(a)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(b))
    print('************')
    # 对于二维矩阵，axis=0轴可以理解为行增长方向（向下）,axis=1轴可以理解为列增长方向(向右）
    print(sess.run(tf.reduce_max(b, axis=1, keepdims=False)))  # keepdims =False,axis=1被消减
    print('************')
    print(sess.run(tf.reduce_max(b, axis=1, keepdims=True)))
    print('************')
    print(sess.run(tf.reduce_max(b, axis=0, keepdims=True)))


# 首先0代表的是行，1代表的是列。#
# 矩阵都是按照0，然后1，最后2的位置进行排列。


"""
[[1 2]
 [5 3]
 [2 6]]
************
[2 5 6]
************
[[2]
 [5]
 [6]]
************
[[5 6]]

"""