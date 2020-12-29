import tensorflow as tf
import numpy as np

#  Computes the maximum of elements across dimensions of a tensor. (deprecated arguments)

#
#  tf.reduce_max(
#      input_tensor,
#      axis=None,
#      keepdims=None,
#      name=None,
#      reduction_indices=None,
#      keep_dims=None
#      )

c = np.array([[3., 4],
              [5., 6],
              [6., 7]])
step = tf.reduce_max(c, 0)
with tf.Session() as sess:
    print(sess.run(step))



    # [6. 7.]