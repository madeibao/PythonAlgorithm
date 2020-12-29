
import tensorflow as tf
a = tf.constant([[1, 2, 3],
                 [4, 5, 6]])

b = tf.constant([[7, 8, 9],
                 [0, 1, 7]])

ab = tf.stack([a, b], axis=0)    # shape (2,2,3)
a1, a2 = tf.unstack(ab, axis=0)

with tf.Session() as sess:
    print(sess.run(a1))
    print(sess.run(a2))


"""


[[1 2 3]
 [3 4 5]]

 
[[ 7  8  9]
 [10 11 12]]

"""