import tensorflow as tf
import numpy as np


def dynamic_rnn(rnn_type='lstm'):
    # 创建输入数据,3代表batch size,6代表输入序列的最大步长(max time),4代表每个序列的维度
    # 有时候最大的步长，代表的就是一个句子的最大的序列的长度。
    X = np.random.randn(3, 6, 4)

    # 第二个输入的实际长度为4
    X[1, 4:] = 0
    # 记录三个输入的实际步长
    X_lengths = [6, 4, 6]

    rnn_hidden_size = 5  # 隐藏层的维数数据。
    if rnn_type == 'lstm':
        cell = tf.contrib.rnn.BasicLSTMCell(num_units=rnn_hidden_size, state_is_tuple=True)
    else:
        cell = tf.contrib.rnn.GRUCell(num_units=rnn_hidden_size)


    outputs, last_states = tf.nn.dynamic_rnn(
        cell=cell,
        dtype=tf.float64,
        sequence_length=X_lengths,
        inputs=X)

    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        o1, s1 = session.run([outputs, last_states])
        print(np.shape(o1))  #输出的形状为(3, 6, 5)
        print(o1)
        print(np.shape(s1))  #输出的形状为(2, 3, 5)
        print(s1)



# s1一共由两部分组成，
# s1.c和s1.h
# 所以第一个维度是2，第二个维度是批次，本次实验一共有三个批次，分别为【6，4，6】，第二个维度为3
# 隐藏层的单元的个数5，所以输出的第三个维度为5.



if __name__ == '__main__':
    dynamic_rnn(rnn_type='lstm')