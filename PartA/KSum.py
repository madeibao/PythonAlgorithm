
# 沿着指定轴计算张量之和
from keras import backend as K
import numpy as np
import tensorflow as tf
a = np.arange(0, 6).reshape(2, 3)

# [[0 1 2]
#  [3 4 5]]
sum_a_keepdims = K.sum(a, axis=-1, keepdims=True)	   # 保持原来的维度数据。
sum_a_nokeepdims = K.sum(a, axis=-1, keepdims=False)   # 不保持原来的维度

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(sum_a_keepdims))
    print(sess.run(sum_a_nokeepdims))



# [[ 3]
#  [12]]
# [ 3 12]














