import tensorflow as tf
import numpy as np

A = np.array([[[1, 1, 1, 1],
               [2, 2, 2, 2]],
              [[3, 3, 3, 2],
               [4, 4, 4, 4]],
              [[5, 5, 5, 5],
               [6, 6, 6, 6]]])  # 这种是3-D维度的张量。
# A的形状是  #(3—2—4)  # 这种的没有什么变化。

A2 = np.array([[[1, 1, 1, 1]],
               [[3, 3, 3, 2]],
               [[5, 5, 5, 5]]])  # 这种是3-D维度的张量。
# A2的形状是  #(3—1—4)
temp = tf.squeeze(A)    # temp的维度是(3-2-4)
temp2 = tf.squeeze(A2)   # temp2的维度是(3-4)

with tf.Session() as sess:
    print(sess.run(temp))
    print(sess.run(tf.shape(temp)))
    print("----------------------")
    print(sess.run(temp2))
    print(sess.run(tf.shape(temp2)))
    print("----------------------")
    print(sess.run(tf.shape(A2)))
    print(sess.run(tf.shape(A)))





# [[[1 1 1 1]
#   [2 2 2 2]]

#  [[3 3 3 2]
#   [4 4 4 4]]

#  [[5 5 5 5]
#   [6 6 6 6]]]
# [3 2 4]
# ----------------------
# [[1 1 1 1]
#  [3 3 3 2]
#  [5 5 5 5]]
# [3 4]
# ----------------------
# [3 1 4]
# [3 2 4]


# 去掉维数为1的维度,降维 
#    For example:
#   # 't' is a tensor of shape [1, 2, 1, 3, 1, 1]
#   shape(squeeze(t)) ==> [2, 3]12
# Or, to remove specific size 1 dimensions:
#   # 't' is a tensor of shape [1, 2, 1, 3, 1, 1]
#   shape(squeeze(t, [2, 4])) ==> [1, 2, 3, 1]
