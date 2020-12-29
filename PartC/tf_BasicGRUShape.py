
import tensorflow as tf
batch_size=10
depth=128
output_dim=100
inputs=tf.Variable(tf.random_normal([batch_size,depth]))
previous_state=tf.Variable(tf.random_normal([batch_size,output_dim])) #前一个状态的输出
gruCell=tf.nn.rnn_cell.GRUCell(output_dim)
output,state=gruCell(inputs,previous_state)
print(output)
print(state)


"""
Tensor("gru_cell/add:0", shape=(10, 100), dtype=float32)
Tensor("gru_cell/add:0", shape=(10, 100), dtype=float32)

"""