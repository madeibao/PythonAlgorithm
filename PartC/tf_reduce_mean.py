import tensorflow as tf

x = [[1, 2, 3],
     [1, 2, 3]]

xx = tf.cast(x, tf.float32)
mean_all = tf.reduce_mean(xx, keep_dims=True)
mean_0 = tf.reduce_mean(xx, axis=0, keep_dims=True)   #每列取平均值。
mean_1 = tf.reduce_mean(xx, axis=1, keep_dims=True)   #每行取平均值。

with tf.Session() as sess:
    m_a, m_0, m_1 = sess.run([mean_all, mean_0, mean_1])   # 一次可以运行多个张量。

print(m_a)
print(m_0)
print(m_1)


# keep_dims=True 表示的是使得原来的能够保持原来的维度和数据。

# axis=0代表往跨行（down)，而axis=1代表跨列（across)，作为方法动作的副词（译者注）

"""
输出结果为：


[[2.]]

[[1. 2. 3.]]


[[2.]
 [2.]]

"""




