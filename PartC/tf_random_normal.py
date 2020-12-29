import tensorflow as tf

w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(w1))



"""
输出的结果为
[[-0.8113182   1.4845988   0.06532937]
 [-2.4427042   0.0992484   0.5912243 ]]

 
"""



# tf.random_normal(
#     shape,
#     mean=0.0,
#     stddev=1.0,
#     dtype=tf.float32,
#     seed=None,
#     name=None
# )

# shape: 输出张量的形状，必选
# mean: 正态分布的均值，默认为0
# stddev: 正态分布的标准差，默认为1.0
# dtype: 输出的类型，默认为tf.float32
# seed: 随机数种子，是一个整数，当设置之后，每次生成的随机数都一样
# name: 操作的名称