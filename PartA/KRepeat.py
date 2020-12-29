from keras import backend as K
import tensorflow as tf

x2 = K.constant([[1, 1, 1, 1],
                 [2, 2, 2, 2],
                 [2, 3, 5, 8]], dtype=tf.float32)   # 2-D 维度的张量设置。

temp = K.repeat(x2, 3)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(temp))



# 重复2D张量，例如若xshape是(samples, dim)且n为2，则输出张量的shape是(samples, 2, dim)
# 2D 维度的张量，重复的设置。
# [[[1. 1. 1. 1.]
#   [1. 1. 1. 1.]
#   [1. 1. 1. 1.]]

#  [[2. 2. 2. 2.]
#   [2. 2. 2. 2.]
#   [2. 2. 2. 2.]]

#  [[2. 3. 5. 8.]
#   [2. 3. 5. 8.]
#   [2. 3. 5. 8.]]]