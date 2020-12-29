

# -*- coding: utf-8 -*-

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

 

# 载入依赖库

import tensorflow as tf

import numpy as np

 

# 读取MNIST数据集

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('F:/pythonWorkSpace/mnistTest/data', one_hot=True)

 

 

# 设置训练参数

learning_rate = 0.01

max_samples = 400000

batch_size = 128

display_step = 10

 

# 设置网络结构参数

n_input = 28  # MNIST数据输入(img shape: 28*28)

n_steps = 28  # timesteps

n_hidden = 256  # LSTM的隐藏节点数

n_classes = 10  # MNIST数据集分类数目

 

# 创建输入x和学习目标y的placeholder

x = tf.placeholder("float", [None, n_steps, n_input])
y = tf.placeholder("float", [None, n_classes])

# 创建最后的Softmax层的weights和biases

weights = {
    'out': tf.Variable(tf.random_normal([2 * n_hidden, n_classes]))
}
biases = {
    'out': tf.Variable(tf.random_normal([n_classes]))
}

 

# 定义网络的生成函数

def BiRNN(x, weights, biases):

    x = tf.transpose(x, [1, 0, 2])
    x = tf.reshape(x, [-1, n_input])
    x = tf.split(x, n_steps)

 

    # 创建forward和backword的LSTM单元

    lstm_fw_cell = tf.contrib.rnn.BasicLSTMCell(n_hidden, forget_bias=1.0)
    lstm_bw_cell = tf.contrib.rnn.BasicLSTMCell(n_hidden, forget_bias=1.0)

 

    # 获得LSTM单元输出

    outputs, _, _ = tf.contrib.rnn.static_bidirectional_rnn(lstm_fw_cell, lstm_bw_cell, x, dtype=tf.float32)

    return tf.matmul(outputs[-1], weights['out']) + biases['out']

 

 

pred = BiRNN(x, weights, biases)
# 定义损失和优化器

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# 评价模型

correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
# 初始化
init = tf.global_variables_initializer()

# 执行训练和测试操作
with tf.Session() as sess:

    sess.run(init)

    step = 1

    # 保持训练直到达到最大迭代次数

    while step * batch_size < max_samples:

        batch_x, batch_y = mnist.train.next_batch(batch_size)
        batch_x = batch_x.reshape((batch_size, n_steps, n_input))
        sess.run(optimizer, feed_dict={x: batch_x, y: batch_y})

        if step % display_step == 0:

            # 计算batch accuracy

            acc = sess.run(accuracy, feed_dict={x: batch_x, y: batch_y})

            # 计算batch loss

            loss = sess.run(cost, feed_dict={x: batch_x, y: batch_y})

            print("Iter " + str(step * batch_size) + ", Minibatch Loss= " + \

                  "{:.6f}".format(loss) + ", Training Accuracy= " + \

                  "{:.5f}".format(acc))

        step += 1

    print("Optimization Finished!")
    # 测试数据，并展示准确率
    test_len = 10000
    test_data = mnist.test.images[:test_len].reshape((-1, n_steps, n_input))
    test_label = mnist.test.labels[:test_len]
    print("Testing Accuracy:", sess.run(accuracy, feed_dict={x: test_data, y: test_label}))










    
