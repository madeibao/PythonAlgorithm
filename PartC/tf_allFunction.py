
import numpy as np
import tensorflow as tf
from keras import backend as K


init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(temp))



A = np.array([[[1, 1, 1, 1],
               [2, 2, 2, 2]],
              [[3, 3, 3, 2],
               [4, 4, 4, 4]],
              [[5, 5, 5, 5],
               [6, 6, 6, 6]]])  # 这种是3-D维度的张量。 (3-2-4)维度的张量.

A2 = np.array([[[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [2, 4, 6, 8, 10]],
               [[1, 4, 3, 5, 7],
                [2, 4, 2, 3, 2],
                [9, 6, 9, 4, 7]]])  # 这种是3-D维度的张量。(2-3-5)


x = tf.constant([[1., 2., 3.],
                 [1., 5., 3.],
                 [1., 2., 9.]], dtype=tf.float32)  # 2-D维度的张量。


x2 = tf.constant([[[1, 1, 1, 1],
                   [2, 2, 2, 2],
                   [2, 3, 5, 8]],
                  [[3, 3, 3, 2],
                   [4, 4, 4, 4],
                   [2, 1, 2, 4]],
                  [[5, 5, 5, 5],
                   [6, 6, 6, 6],
                   [2, 1, 6, 9]]], dtype=tf.float32)  #3-3-4的张量维度数据。

x3 = tf.constant([[[1, 1, 1, 1],
                   [2, 3, 5, 8]],
                  [[3, 3, 3, 2]],
                  [[5, 5, 5, 5]]], dtype=tf.float32)

 # 创建输入数据,3代表batch size,2代表输入序列的最大步长(max time),4代表每个序列的维度
    # 有时候最大的步长，代表的就是一个句子的最大的序列的长度。


# 可以通过一个矩阵的初始化的操作来实现3——D维度的张量的运算。
# 例如：
X = np.random.randn(3, 6, 4)

init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)



