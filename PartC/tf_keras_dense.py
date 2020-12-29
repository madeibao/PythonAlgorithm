

import io
import numpy as np
import tensorflow as tf
inputs = tf.ones([2, 3])
a = tf.layers.dense(inputs, 4)
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    print(sess.run(inputs))
    print(sess.run(a))


# 输出结果为

"""
[[1. 1. 1.]
 [1. 1. 1.]]
[[-1.5794101   0.69538873 -0.9422083   0.6114345 ]
 [-1.5794101   0.69538873 -0.9422083   0.6114345 ]]

"""



"""
self.dense = tf.keras.layers.Dense(units=1, kernel_initializer=tf.zeros_initializer(),
bias_initializer=tf.zeros_initializer())


units: Positive integer, dimensionality of the output space.
activation: Activation function to use. If you don’t specify anything, no activation is applied (ie. “linear” activation: a(x) = x).
use_bias: Boolean, whether the layer uses a bias vector.
kernel_initializer: Initializer for the kernel weights matrix.
bias_initializer: Initializer for the bias vector.

这个全连接层封装了output = activation(tf.matmul(input, kernel) + bias)
这一线性变换+激活函数的计算操作，以及 kernel 和 bias 两个变量。当不指定激活函数时（即 activation(x) = x ），这个全连接
层就等价于我们上述的线性变换。
一提，全连接层可能是我们编写模型时使用最频繁的层。

"""