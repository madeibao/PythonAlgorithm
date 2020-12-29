import tensorflow as tf

v1 = tf.Variable(tf.random_normal(shape=[4, 3], mean=0, stddev=1), name='v1')
v2 = tf.Variable(tf.constant(2), name='v2')
v3 = tf.Variable(tf.ones([4, 3]), name='v3')
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())   # 全局的变量内容进行初始化的操作。
    print(sess.run(v1))
    print(sess.run(v2))
    print(sess.run(v3))

# 这里需要注意的是：tf.Variable(initializer,name),参数initializer是初始化参数，name是可自定义的变量名称，用法如下：


# 结果如下所示:
# [[-9.3692186e-05  1.0147363e+00 -2.6339817e-01]
#  [ 8.2593310e-01 -4.4634894e-01 -4.8594180e-01]
#  [-1.3387115e-01  1.9202982e-01  1.2812712e+00]
#  [ 5.8659726e-01  5.2299666e-01 -9.1439164e-01]]
# 2
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]


# 一：tf.Variable
# tf.Variable主要用于可训练的一些变量，比如模型的权重（weight ，w）,模型的偏置值（bias,b）
# 1.声明时必须要进行初始化
# 2.名称的真实含义在于变量，也就是在训练时，其值是可以改变的