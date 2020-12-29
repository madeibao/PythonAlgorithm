import tensorflow as tf

lstm_cell = tf.contrib.rnn.BasicLSTMCell(num_units=128, forget_bias=1.0, state_is_tuple=True, activation=None, reuse=None, name=None)
print(lstm_cell.output_size)  # 128
print(lstm_cell.state_size)   # LSTMStateTuple(c=128, h=128)

inputs = tf.placeholder(shape=[32, 100], dtype=tf.float32)  # 32 是 batch_size
h0 = lstm_cell.zero_state(batch_size=32, dtype=tf.float32)
print(h0)

# LSTMStateTuple(c=<tf.Tensor 'BasicLSTMCellZeroState/zeros:0' shape=(32, 128) dtype=float32>, h=<tf.Tensor 'BasicLSTMCellZeroState/zeros_1:0' shape=(32, 128) dtype=float32>)

new_h, new_state = lstm_cell(inputs=inputs, state=h0)   # 调用 call 函数, 在时间序列上推进一步
print(new_h.shape)  # (32, 128)
print(new_state.h)  # Tensor("mul_2:0", shape=(32, 128), dtype=float32)
print(new_state.c)  # Tensor("add_1:0", shape=(32, 128), dtype=float32)


