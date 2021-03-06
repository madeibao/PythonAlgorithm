import tensorflow as tf

import numpy as np
cell = tf.nn.rnn_cell.BasicRNNCell(num_units=128)   # state_size = 128
print(cell.state_size)    # 128

inputs = tf.placeholder(np.float32, shape=(32, 100))   # 32 是 batch_size
h0 = cell.zero_state(32, np.float32)   # 通过zero_state得到一个全0的初始状态，形状为(batch_size, state_size)
output, h1 = cell.__call__(inputs, h0)   # 调用call函数
print(h1.shape)   # (32, 128)




"""

输出结果为：

128
(32, 128)

"""