import tensorflow as tf

output_dim = 128
lstm = tf.nn.rnn_cell.BasicLSTMCell(output_dim)
batch_size = 10  # 批处理大小
timesteps = 45  # 时间步长
embedding_dim = 300  # 词向量维度

inputs = tf.Variable(tf.random_normal([batch_size, embedding_dim]))
previous_state = (tf.random_normal(shape=(batch_size, output_dim)), tf.random_normal(shape=(batch_size, output_dim)))
# 先前的两个输出的状态。
# 分别代表的是一个是Ct和Ht,两个以前的输出的状态。

output, (new_h, new_state) = lstm(inputs, previous_state)  # 先前的输入的状态送入神经网络结构。
print(output.shape)  # (10, 128)
print(new_h.shape)  # (10, 128)
print(new_state.shape)  # (10, 128)




