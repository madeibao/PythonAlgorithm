
import tensorflow as tf
a1 = tf.constant([[1, 3, 2], [2, 2, 4]])
a = tf.sequence_mask(a1, 5)
a2 = tf.cast(a, tf.float32)
with tf.Session() as sess:
    print(sess.run(a))
    print(sess.run(tf.shape(a)))    # 2-3-5
    print(sess.run(tf.shape(a1)))   # 2-3
    print(sess.run(a2))




# [[[ True False False False False]
#   [ True  True  True False False]
#   [ True  True False False False]]

#  [[ True  True False False False]
#   [ True  True False False False]
#   [ True  True  True  True False]]]
# [2 3 5]
# [2 3]
# [[[1. 0. 0. 0. 0.]
#   [1. 1. 1. 0. 0.]
#   [1. 1. 0. 0. 0.]]

#  [[1. 1. 0. 0. 0.]
#   [1. 1. 0. 0. 0.]
#   [1. 1. 1. 1. 0.]]]
