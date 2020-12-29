


import tensorflow as tf
a = tf.constant([2, 3, 1, 2, 3, 2, 1])
b = tf.constant([[0, 1],
                 [2, 3],
                 [3, 0],
                 [4, 0],
                 [5, 0],
                 [6, 1],
                 [2, 4]])


mul = tf.reduce_sum(tf.multiply(a, tf.transpose(b, perm=[1, 0])), reduction_indices=1)
with tf.Session() as sess:
	print(sess.run(mul))

# [46 17]

