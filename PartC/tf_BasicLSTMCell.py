import tensorflow as tf
import numpy as np


# 产生3个batch数据，句子length为2，embedding大小为4
batch_size = 3   # 批次的大小
input_dim = 2    # 输入的维度数据
output_dim = 6   # 输出的维度数据。

inputs = tf.placeholder(dtype=tf.float32, shape=(batch_size, input_dim))  # 只是占位符，并不是真正的赋值。
previous_state = (tf.random_normal(shape=(batch_size, output_dim)), tf.random_normal(shape=(batch_size, output_dim)))

cell = tf.contrib.rnn.BasicLSTMCell(num_units=output_dim)  # num_units 代表的是隐藏层的单元的个数。最后的输出的维度首次影响。
output, (state_c, state_h) = cell(inputs, previous_state)

X = np.ones(shape=(batch_size, input_dim))  # 首先是矩阵的初始化的操作。
"""
    # (3,6)的输入的形式。

"""
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())  # 全局的变量的初始化的操作。
    o, s_c, s_h = sess.run([output, state_c, state_h], feed_dict={inputs: X})
    print(X)
    print("第一部分的值")
    print(previous_state[0].eval())
    print("第二部分的值")
    print(previous_state[1].eval())
    print("----------------------")
    print("：：：：：：：：：：：")
    print(o)                        # (3,6)
    print("：：：：：：：：：：：")
    print(s_c)                      # (3,6)
    print("：：：：：：：：：：：")
    print(s_h)                      # (3,6)




"""

[[1. 1.]
 [1. 1.]
 [1. 1.]]
第一部分的值
[[ 1.6649199   1.7594844   0.8973156  -1.1239377   0.46506456  0.2641916 ]
 [ 0.602965    2.612344    2.2393146   1.3881977   2.7179     -0.9793957 ]
 [ 1.0932682   1.7715838   2.7497098  -0.09541277 -0.65734583 -0.12410627]]
第二部分的值
[[-0.6481396  -0.9520873  -0.18432198  0.23224422  0.06232261  1.6073548 ]
 [-0.25546357 -0.16183135  0.60944915 -1.3807259  -0.7564184  -1.0225828 ]
 [ 0.5091772  -0.39213467  0.31147608 -0.72876704 -0.3016867  -0.03878614]]
----------------------
：：：：：：：：：：：
[[ 0.04485227  0.21375757  0.07028335  0.07218743 -0.39670116  0.2703328 ]
 [-0.03542977 -0.33840975 -0.43325633  0.32124794 -0.11900812  0.08261754]
 [ 0.07295127  0.08617558  0.04020087 -0.24593441 -0.4312762  -0.06538878]]
：：：：：：：：：：：
[[ 0.09316626  0.39066076  0.10929778  0.12840103 -0.80249846  0.42767143]
 [-0.04613803 -0.9074882  -1.0874608   0.75580394 -0.33822906  0.30402684]
 [ 0.12967838  0.1431885   0.07744437 -0.44327703 -1.3721142  -0.11076972]]
：：：：：：：：：：：
[[ 0.04485227  0.21375757  0.07028335  0.07218743 -0.39670116  0.2703328 ]
 [-0.03542977 -0.33840975 -0.43325633  0.32124794 -0.11900812  0.08261754]
 [ 0.07295127  0.08617558  0.04020087 -0.24593441 -0.4312762  -0.06538878]]



"""