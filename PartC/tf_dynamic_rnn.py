import tensorflow as tf
import numpy as np

# 产生2个batch数据，句子length为3，embedding大小为4
X = np.random.randn(2, 3, 4) 

# 第二个batch长度为2
X[1, 2:] = 0
X_lengths = [3, 2]  # 第一个长度为3，第二个长度为2，所有要填充。
print(X)

cell = tf.nn.rnn_cell.BasicLSTMCell(num_units=2, state_is_tuple=True)  # 官方建议设置为True。

# num_units=2 代表的就是   int型, LSTM网络单元的个数，即隐藏层的节点数。

outputs, last_states = tf.nn.dynamic_rnn(  # 返回输出的结果和最后的一个结果的状态。
    cell=cell,
    dtype=tf.float64,
    sequence_length=X_lengths,
    inputs=X)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    o = sess.run(outputs)
    s = sess.run(last_states)       # 最后的一个状态。

    print('output\n', o)
    print('last_o\n', o[:, -1, :])  # 从output中取最后一次输出

    print('--------------------------')
    print('s\n', s)
    print('s.c\n', s.c)  # 这是门控制单元的权重，这里不需要
    print('s.h\n', s.h)  # s.h就是最后一次输出的状态

"""
    输出的结果：


output
输出的结果为2-3-2

2代表的是测试有两个批次，第一个长度为3，第二个长度为2.
3代表的是句子的的长度为3.也就是一句话中有3个单词。
2代表的是num_units=2,也就是嵌入层的维度数据，如果num_units=3，那么输出也就变成了2-3-3


 [[[ 1.59743651e-02  6.82441454e-02]
  [-7.40925855e-02  2.09460537e-02]
  [ 1.09100742e-02  7.96369685e-05]]

 [[ 1.18962740e-01 -4.12714336e-02]
  [ 1.80561538e-01 -3.68809194e-03]
  [ 0.00000000e+00  0.00000000e+00]]]
last_o
 [[1.09100742e-02 7.96369685e-05]
 [0.00000000e+00 0.00000000e+00]]
--------------------------
s
 LSTMStateTuple(c=array([[ 2.03634914e-02,  1.61167030e-04],
       [ 4.09042725e-01, -6.54977309e-03]]), h=array([[ 1.09100742e-02,  7.96369685e-05],
       [ 1.80561538e-01, -3.68809194e-03]]))
s.c
 [[ 2.03634914e-02  1.61167030e-04]
 [ 4.09042725e-01 -6.54977309e-03]]
s.h
 [[ 1.09100742e-02  7.96369685e-05]
 [ 1.80561538e-01 -3.68809194e-03]]


"""