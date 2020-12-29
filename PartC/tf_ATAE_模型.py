
import tensorflow as tf

inputs = tf.constant([[[1, 1, 1, 1],
                       [2, 2, 2, 2],
                       [0, 0, 0, 0]],
                      [[3, 3, 3, 2],
                       [4, 4, 4, 4],
                       [2, 1, 2, 4]],
                      [[5, 5, 5, 5],
                       [6, 6, 6, 6],
                       [2, 1, 6, 9]]], dtype=tf.int32)


target = tf.constant([[[1, 1, 1, 1]],
                      [[3, 3, 3, 2]],
                      [[5, 5, 5, 5]]], dtype=tf.int32)

target = tf.reshape(target, [-1, 1, 4])
batch_size = tf.shape(inputs)[0]
x3 = tf.ones([batch_size, 3, 4], dtype=tf.int32)

target = tf.multiply(target, x3)
inputs = tf.concat([inputs, target], 2)   # 第二个维度进行级联的操作。


sess = tf.Session()
print(sess.run(x3))
print("~~~~~~~~~~~~~~~~~~~~")
print(sess.run(target))
print("~~~~~~~~~~~~~~~~~~~~")
print(sess.run(inputs))



# [[[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]

#  [[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]

#  [[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]]
# [[[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]

#  [[3 3 3 2]
#   [3 3 3 2]
#   [3 3 3 2]]

#  [[5 5 5 5]
#   [5 5 5 5]
#   [5 5 5 5]]]
# [[[1 1 1 1 1 1 1 1]
#   [2 2 2 2 1 1 1 1]
#   [0 0 0 0 1 1 1 1]]

#  [[3 3 3 2 3 3 3 2]
#   [4 4 4 4 3 3 3 2]
#   [2 1 2 4 3 3 3 2]]

#  [[5 5 5 5 5 5 5 5]
#   [6 6 6 6 5 5 5 5]
#   [2 1 6 9 5 5 5 5]]]
