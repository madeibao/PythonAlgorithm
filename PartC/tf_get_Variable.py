# tf.Variable()用于生成一个初始值为initial-value的变量；必须指定初始化值。
# tf.get_variable()获取已存在的变量(要求不仅名字，而且初始化方法等各个参数都一样)，如果不存在，就新建一个；可以用各种初始化方法，不用明确指定值。



# tf.Variable() Variable 且以大写字母开头，该函数在于定义一个变量
import tensorflow as tf

a1 = tf.Variable(1, name='a1')                                                 # 用变量初始化
a2 = tf.Variable(tf.constant(1), name='a2')                                    # 用变量初始化
a3 = tf.Variable(tf.random_normal(shape=[2, 3], mean=0, stddev=1), name='a3')  # 用随机数初始化
a4 = tf.Variable(tf.ones(shape=[2, 3]), name='a4')                             # 用one矩阵初始化

init = tf.global_variables_initializer()  # 输出数据时必须要全局初始化
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(a1))
    print(sess.run(a2))
    print(sess.run(a3))





# tf.get_variable()：可根据 name 值，返回该变量，如果该 name 不存在的话，则会进行创建；

# 定义常量
a5 = tf.get_variable(name='a5', initializer=22)
# 定义正态分布的随机变量
a6 = tf.get_variable(name='a6', shape=[2, 3], initializer=tf.random_normal_initializer(mean=0, stddev=1))
# 定义常量向量
a7 = tf.get_variable(name='a7', shape=[2], initializer=tf.constant_initializer(1))
# 全是1的矩阵
a8 = tf.get_variable(name='a8', shape=[2, 3], initializer=tf.ones_initializer())   # 随机的初始化值全部为1.
init = tf.global_variables_initializer()  # 输出数据时必须要全局初始化
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(a5))
    print(sess.run(a6))
    print(sess.run(a7))
    print(sess.run(a8))


"""
下面的部分的输出的结果为：

22
[[ 1.4098579  -1.0918872  -0.8145695 ]
 [ 0.51305777 -1.3569524  -1.7222371 ]]
[1. 1.]
[[1. 1. 1.]
 [1. 1. 1.]]
"""