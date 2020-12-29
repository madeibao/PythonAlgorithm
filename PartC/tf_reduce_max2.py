import tensorflow as tf

# tf.reduce_max 计算张量的各个维度上元素的最大值

x = tf.constant([[1, 2, 3],
                 [4, 5, 6]])

with tf.Session() as sess:
    print(sess.run(tf.reduce_max(x)))
    print(sess.run(tf.reduce_max(x, 0)))
    print(sess.run(tf.reduce_max(x, 1)))
    print(sess.run(tf.reduce_max(x, 1, keepdims=True)))
    print(sess.run(tf.reduce_max(x, [0, 1])))



# 6
# [4 5 6]
# [3 6]
# [[3]
#  [6]]
# 6
# 6






