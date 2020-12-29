import tensorflow as tf
import numpy as np

# 创建输入数据,3代表batch size,6代表输入序列的最大步长(max time),4代表每个序列的维度
# 有时候最大的步长，代表的就是一个句子的最大的序列的长度。
X = np.random.randn(4, 6, 4)  # 输入的这个维度。 第一个4代表的是批次，一共4组训练数据。随机的进行初始化的操作。

# 第二个输入的实际长度为4
X[1, 4:] = 0
# 记录三个输入的实际步长
X_lengths = [6, 4, 6, 5]  # 一共有4个批次，所有这里有4个维度。
rnn_hidden_size = 5  # 隐藏层的维数数据。所以第三个维度的数据为5.
cell = tf.contrib.rnn.GRUCell(num_units=rnn_hidden_size)   # 基本的GRU的模块单元内容。

outputs, last_states = tf.nn.dynamic_rnn(
    cell=cell,
    dtype=tf.float64,
    sequence_length=X_lengths,
    inputs=X)

with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    o1, s1 = session.run([outputs, last_states])
    print(np.shape(o1))
    print(o1)
    print(np.shape(s1))
    print(s1)



"""
GRU的模块的输入和输出结果为：

(4, 6, 5)
[[[-0.1663887   0.0679706   0.0019297  -0.06090882 -0.04307698]
  [-0.3926528   0.15783012 -0.34175198 -0.00424352  0.00391389]
  [-0.4754058   0.20826476 -0.31169857 -0.20015663 -0.16807073]
  [-0.31033449  0.13693115 -0.27346733 -0.08988369 -0.2958693 ]
  [ 0.01545392  0.12420134 -0.42533294  0.01635332 -0.15268687]
  [ 0.07426556 -0.01059626 -0.06933272  0.16280032  0.0112538 ]]

 [[ 0.12140121 -0.04625256  0.20493182  0.04231962  0.3674238 ]
  [ 0.28080309 -0.41003275  0.35622585 -0.01022669  0.52745891]
  [ 0.19360472 -0.24981837  0.33320325 -0.03696296  0.36374773]
  [ 0.09665677 -0.07441859  0.3107747  -0.14493954  0.29409472]
  [ 0.          0.          0.          0.          0.        ]
  [ 0.          0.          0.          0.          0.        ]]

 [[ 0.16334039 -0.09095972 -0.04187129  0.08120718  0.12325531]
  [ 0.13130156 -0.01833198 -0.15018865  0.11991364  0.33423411]
  [ 0.0860955   0.0361017  -0.02932471  0.16607676  0.0505418 ]
  [ 0.19543999 -0.08676367  0.21922737  0.19661322  0.41624886]
  [ 0.22517798 -0.21156023  0.28636411 -0.0085371   0.41024593]
  [ 0.11273674 -0.14579388  0.31954971 -0.35703002  0.37168368]]

 [[-0.28303516  0.12382577  0.01397025 -0.12188152 -0.17335398]
  [-0.40295569  0.24020264 -0.47131945 -0.05649001  0.03084141]
  [-0.35536405 -0.03241655 -0.37498143 -0.22542104 -0.17644021]
  [-0.14597485 -0.29692656 -0.22981852 -0.21111844 -0.12810135]
  [-0.23888566 -0.15187787 -0.21246115 -0.18567198 -0.31814853]
  [ 0.          0.          0.          0.          0.        ]]]



(4, 5)  # 代表的是最后的一个输出的状态。5代表的是维度数据。
[[ 0.07426556 -0.01059626 -0.06933272  0.16280032  0.0112538 ]
 [ 0.09665677 -0.07441859  0.3107747  -0.14493954  0.29409472]
 [ 0.11273674 -0.14579388  0.31954971 -0.35703002  0.37168368]
 [-0.23888566 -0.15187787 -0.21246115 -0.18567198 -0.31814853]]

Process finished with exit code 0


"""







