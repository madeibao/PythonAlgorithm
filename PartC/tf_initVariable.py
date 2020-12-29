import tensorflow as tf

# 1.计算机的伪随机数是由随机种子根据一定的计算方法计算出来的数值。所以，只要计算方法一定，随机种子一定，那么产生的随机数就是固定的。
# 2.只要用户或第三方不设置随机种子，那么在默认情况下随机种子来自系统时钟。
# 均匀分布

A = tf.random_uniform(shape=[1, 10], minval=0, maxval=1, dtype=tf.float32, seed=2)
# B = tf.Variable(A, )
# 截断正态分布, 采样时当样本偏离均值两个标准差时, 放弃本次采样样本, 重新采样
B = tf.truncated_normal([2, 2], mean=0.0, stddev=1.0, dtype=tf.float32, seed=100)
# 正态分布
C = tf.random_normal([2, 2], mean=0.0, stddev=1.0, dtype=tf.float32, seed=1000)
# 0
D = tf.zeros([2, 2], dtype=tf.float32)
# 1
E = tf.ones([2, 2], dtype=tf.float32)
# 常量

F = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
G = tf.constant(3, dtype=tf.float32, shape=[2, 2])
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())
print(A.eval())
print(B.eval())
print(C.eval())
print(D.eval())
print(E.eval())
print(F.eval())
print(G.eval())
sess.close()











