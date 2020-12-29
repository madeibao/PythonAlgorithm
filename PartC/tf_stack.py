
import tensorflow as tf
a = tf.constant([[1, 2, 3],
                 [4, 5, 6]])
b = tf.constant([[7, 8, 9],
                 [0, 1, 7]])
c = tf.stack([a, b], axis=0)
d = tf.stack([a, b], axis=1)
with tf.Session() as sess:
    result1 = sess.run(c)
    print(result1)
    print(sess.run(d))





"""
[[[1 2 3]
  [4 5 6]]

 [[7 8 9]
  [0 1 7]]]
[[[1 2 3]
  [7 8 9]]

 [[4 5 6]
  [0 1 7]]]



"""