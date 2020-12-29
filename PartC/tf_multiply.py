import tensorflow as tf

x = tf.constant([[1, 2, 3],
                 [1, 2, 3],
                 [1, 2, 3]])

y = tf.constant([[1, 2, 3],
                 [1, 2, 3],
                 [1, 2, 3]])


xy = tf.multiply(x, y)
with tf.Session() as sess:
    print(sess.run(xy))



# 一个矩阵中的对应位置的元素进行相乘。

# [[1 4 9]
#  [1 4 9]
#  [1 4 9]]

