import tensorflow as tf

# 't' is a tensor of shape [2]
t = tf.constant([1, 2])
me = tf.constant([[1, 2, 3],
                  [3, 4, 4]])

m4 = tf.constant([[1, 2, 3],
                  [3, 4, 4]])
m4 *= me   # 这里只是对应的位置的相乘.
with tf.Session() as sess:
    print(sess.run(m4))



# [[ 1  4  9]
#  [ 9 16 16]]

