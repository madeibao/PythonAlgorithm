tf.nn.dynamic_rnn(
    cell,
    inputs,
    sequence_length=None,
    initial_state=None,
    dtype=None,
    parallel_iterations=None,
    swap_memory=False,
    time_major=False,
    scope=None
)



 tf.nn.dynamic_rnn的返回值有两个：outputs和state

为了描述输出的形状，先介绍几个变量，batch_size是输入的这批数据的数量，max_time就是这批数据中序列的最长长度，
如果输入的三个句子，那max_time对应的就是最长句子的单词数量，cell.output_size其实就是rnn cell中神经元的个数。

outputs. outputs是一个tensor
如果time_major==True，outputs形状为 [max_time, batch_size, cell.output_size ]（要求rnn输入与rnn输出形状保持一致）
如果time_major==False（默认），outputs形状为 [ batch_size, max_time, cell.output_size ]
state. state是一个tensor。state是最终的状态，也就是序列中最后一个cell输出的状态。
一般情况下state的形状为 [batch_size, cell.output_size ]，
但当输入的cell为BasicLSTMCell时，state的形状为[2，batch_size, cell.output_size ]，其中2也对应着LSTM中的cell state和hidden state
那为什么state输出形状会有变化呢？state和output又有什么关系呢？


我们以LSTM和GRU分别为tf.nn.dynamic_rnn的输入cell类型为例，当cell为LSTM，state形状为[2，batch_size, cell.output_size ]；
当cell为GRU时，state形状为[batch_size, cell.output_size ]。
其原因是因为LSTM和GRU的结构本身不同，
如下面两个图所示，这是LSTM的cell结构，每个cell会有两个输出: 和 ，
上面这个图是输出，代表哪些信息应该被记住哪些应该被遗忘；
下面这个图是输出，代表这个cell的最终输出，LSTM的state是由 和 组成的。




import tensorflow as tf

X = tf.random_normal(shape=[3, 5, 6], dtype=tf.float32)
X = tf.reshape(X, [-1, 5, 6])
cell = tf.nn.rnn_cell.GRUCell(10)
init_state = cell.zero_state(3, dtype=tf.float32)
output, state = tf.nn.dynamic_rnn(cell, X, initial_state=init_state, time_major=False)
with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    print(sess.run(tf.shape(output)))   # 3-5-10
    print(sess.run(output))
    print(sess.run(tf.shape(state)))    # 3-10
    print(sess.run(state))




[ 3  5 10]
[[[ 8.48207101e-02  1.36138111e-01  8.04723576e-02 -6.13811798e-02
   -1.31633461e-01 -1.37800992e-01 -1.31895998e-02 -5.50821573e-02
   -1.18294962e-01 -5.43647148e-02]
  [ 1.49276793e-01  1.56212419e-01 -1.99624956e-01 -2.67635554e-01
    1.66336671e-02 -8.27768296e-02 -7.64900818e-02 -6.55186176e-02
   -1.84464067e-01 -4.44923006e-02]
  [ 5.63007034e-02  7.41844550e-02 -2.10556805e-01 -2.94734329e-01
    1.05294004e-01  6.27418384e-02 -1.84012353e-01 -7.03927726e-02
   -2.35492989e-01 -1.34390295e-02]
  [-4.30752300e-02 -2.47703135e-01 -2.86336958e-01 -8.04966688e-03
    4.06814218e-01  2.12052166e-01 -1.68054804e-01 -1.98653229e-02
    4.37021971e-01 -1.79921463e-02]
  [-1.39647916e-01 -4.48175013e-01 -1.45701885e-01  1.85469210e-01
    4.05196309e-01  1.71111256e-01 -4.82187979e-02 -2.41906807e-01
    5.50622821e-01  5.15302643e-02]]

 [[-1.67672113e-02 -1.07060429e-02  9.61808488e-02 -4.62182574e-02
   -6.43192679e-02 -4.44685817e-01 -1.64108742e-02 -1.54741436e-01
   -2.56267220e-01  2.47062355e-01]
  [ 1.90839171e-04 -1.26026366e-02  1.50213003e-01  4.20100093e-02
   -8.58225077e-02 -3.85946691e-01  1.65725082e-01 -1.43206060e-01
   -1.85272709e-01  5.29400170e-01]
  [ 3.16938311e-01  1.84782058e-01  1.38798922e-01 -5.99777512e-02
   -1.93231702e-01 -3.14366162e-01 -7.43295997e-03 -9.27903056e-02
   -2.15795085e-01  1.91220865e-01]
  [ 5.55732250e-01  2.57125318e-01 -2.52633542e-01 -2.64638484e-01
   -1.16906695e-01 -4.38390672e-03 -1.37645140e-01 -3.00028063e-02
   -1.94700748e-01  3.65909010e-01]
  [ 5.01763701e-01  3.84274423e-01 -1.59740835e-01 -2.19281226e-01
   -1.63060471e-01 -9.76352543e-02 -1.62130207e-01 -5.44564985e-02
   -2.30484188e-01  2.36147389e-01]]

 [[-6.03871532e-02 -1.54511064e-01  1.14251748e-01  1.01211101e-01
   -3.89035679e-02 -2.54580528e-02  2.40988120e-01 -3.62474583e-02
    3.39994282e-02  2.15572834e-01]
  [-8.36082175e-02 -1.24276303e-01  1.44661099e-01  1.80066526e-02
   -3.63377035e-02  2.76920572e-02  1.28152817e-01  1.65093970e-02
    2.01625451e-02  1.09424084e-01]
  [-1.41652167e-01 -3.00749600e-01  2.55356610e-01  2.72842824e-01
    1.49043605e-01 -8.75566155e-02  1.34661809e-01 -2.12304533e-01
    1.54780954e-01  2.72877455e-01]
  [ 2.64257491e-01 -8.85712951e-02  2.20852435e-01  1.08286195e-01
   -4.31970656e-02 -2.75459647e-01  1.26537114e-01 -1.39854372e-01
    9.03621018e-02  1.89248219e-01]
  [ 1.47567332e-01 -1.52314901e-01  2.72738695e-01  1.29237115e-01
    2.86406465e-02 -3.79236102e-01  1.90333650e-02 -2.72546589e-01
    6.26761094e-02  3.44607472e-01]]]

[ 3 10]
[[ 0.21947956  0.35970867 -0.02617349 -0.1834822  -0.22144656 -0.02786946
  -0.35134667  0.00620851 -0.01773123  0.51195574]
 [-0.04782549 -0.11190177  0.21631303  0.08924463 -0.03068072 -0.3619111
   0.1366982   0.03428438 -0.3173144   0.27322146]
 [ 0.02721115  0.07128073  0.09749035  0.1351981  -0.09405419 -0.19161138
   0.22974834 -0.1382414   0.1860089   0.18515386]]
