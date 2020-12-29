

import tensorflow as tf
import numpy as np
A = np.array([[[1, 1, 1, 1],
               [2, 2, 2, 2]],
              [[3, 3, 3, 2],
               [4, 4, 4, 4]],
              [[5, 5, 5, 5],
               [6, 6, 6, 6]]])  # 这种事3-D维度的张量。   3-2-4的维度的张量。


#这个三位的向量为3——2——4
# 产生3个batch数据，句子length为2，embedding大小为4

mn = 2.0 # 代表的是句子的长度的值。

def reduce_mean_with_len(inputs, length):

    """
    :param inputs: 3-D tensor
    :param length: the length of dim [1]
    :return: 2-D tensor
    """
    inputs = tf.cast(inputs, tf.float32)  # 首先转化为浮点形式进行存储。
    length = tf.cast(tf.reshape(length, [-1, 1]), tf.float32) + 1e-9
    inputs = tf.reduce_sum(inputs, 1, keepdims=False) / length  # 除以总的维度数据。
    return inputs


m4 = reduce_mean_with_len(A, mn)

with tf.Session() as sess:
    print(sess.run(m4))


# tf.reduce_sum(inputs, 1, keepdims=False) 调用这个函数的结果为，由于是第二个维度的值。

""" 
# [[ 3  3  3  3]  这里是一个句子的长度值进行相加。
 [ 7  7  7  6]
 [11 11 11 11]]

 除以length长度。
 最终的结果为：2-D 维度的张量。


[[1.5 1.5 1.5 1.5]
 [3.5 3.5 3.5 3. ]
 [5.5 5.5 5.5 5.5]]


"""
