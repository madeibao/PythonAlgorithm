import numpy as np
import keras.backend as K
import tensorflow as tf

t1 = K.variable(np.array([[[1, 2], [2, 3]], [[4, 4], [5, 3]]]))
t2 = K.variable(np.array([[[7, 4], [8, 4]], [[2, 10], [15, 11]]]))

d0 = K.concatenate([t1, t2], axis=0)   # 第零维度的联合。
d1 = K.concatenate([t1, t2], axis=1)
d2 = K.concatenate([t1, t2], axis=2)
d3 = K.concatenate([t1, t2], axis=-1)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(d0))










