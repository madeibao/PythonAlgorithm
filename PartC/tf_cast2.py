
import tensorflow as tf
a = [True, False, False, True]

ac = tf.cast(a, dtype=tf.int32)
with tf.Session() as sess:
    print(sess.run(ac))


# [1 0 0 1]



