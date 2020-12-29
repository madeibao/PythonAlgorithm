
import tensorflow as tf
fw_units = [10, 20, 30]  # 前向传播过程
bw_units = [10, 20, 30]  # 后向传播过程。
fw_cells = [tf.nn.rnn_cell.BasicLSTMCell(unit) for unit in fw_units]  # 前向LSTM层
bw_cells = [tf.nn.rnn_cell.BasicLSTMCell(unit) for unit in bw_units]  # 后向LSTM层

batch_size = 10
max_time = 100
depth = 64

inputs = tf.Variable(tf.random_normal([batch_size, max_time, depth]))
inputs =tf.unstack(inputs, axis=1)

outputs, output_state_fw, output_state_bw =tf.contrib.rnn.stack_bidirectional_rnn(fw_cells, bw_cells, inputs, dtype=tf.float32)

print(len(outputs))    # 100
print(outputs[0].shape)   # (10, 60)
print(outputs[-1].shape)  # (10, 60)
print(len(output_state_fw))  # 3
print(output_state_fw[0].h)
print(output_state_fw[0].c.shape)   # (10, 10)
print(output_state_fw[1].c.shape)   # (10, 20)
print(output_state_bw[0].c.shape)   # (10, 10)
print(output_state_fw[2].h.shape)   # (10, 30)
