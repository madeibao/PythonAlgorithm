# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2019/8/26 13:59
# @File: test826.py
import tensorflow as tf
import numpy as np

X = np.random.randn(2, 10, 8)
# The second example is of length 6
X[1, 6:] = 0
X_lengths = [10, 6]

cell = tf.nn.rnn_cell.GRUCell(num_units=5)  # 通过基本的LSTM网络来构建。

outputs, states = tf.nn.bidirectional_dynamic_rnn(cell_fw=cell, cell_bw=cell, dtype=tf.float64, sequence_length=X_lengths, inputs=X)

output_fw, output_bw = outputs
states_fw, states_bw = states

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    states_shape = tf.shape(states)
    print(states_shape.eval())
    # c = states_fw
    # o = output_fw
    # print('c\n', sess.run(c))
    # print('o\n', sess.run(o))
    print("--------------------------")
    # print(sess.run(tf.shape(outputs)))
    # print(sess.run(tf.shape(output_fw)))
    print(sess.run(tf.shape(states_fw)))
    print(sess.run(tf.shape(states)))




# [2 2 5]
# --------------------------
# [2 5]
# [2 2 5]






