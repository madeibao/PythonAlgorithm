
import tensorflow as tf

batch_size = 4 
input = tf.random_normal(shape=[3, batch_size, 6], dtype=tf.float32)
cell = tf.nn.rnn_cell.BasicRNNCell(10)
init_state = cell.zero_state(batch_size, dtype=tf.float32)
output, final_state = tf.nn.dynamic_rnn(cell, input, initial_state=init_state, time_major=True)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(output).shape)
    print(sess.run(final_state))



"""
输出的形状为（3，4，10）
由于基本的RNN的单元模块是隐藏层的个数为10，
所以输出的结果为10.


"""