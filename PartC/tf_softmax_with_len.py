import tensorflow as tf
import numpy as np
AA = np.array([[[1, 1, 1, 1],
                [2, 2, 2, 2]],
               [[3, 3, 3, 2],
                [4, 4, 4, 4]],
               [[5, 5, 5, 5],
                [6, 6, 6, 6]]])  # 这种是3-D维度的张量。  (3-2-4)

length2 = 15
max_len2 = 24


def softmax_with_len(inputs, length, max_len):
    inputs = tf.cast(inputs, tf.float32)  # 转换成浮点类型的。
    # max_axis = tf.reduce_max(inputs, -1, keep_dims=True)
    # inputs = tf.exp(inputs - max_axis)
    inputs = tf.exp(inputs)
    length = tf.reshape(length, [-1])      # 展平，变成[1 1 1 2 2 2 3 3 3 4 4 4 5 5 5 6 6 6]，这种样式的维数的数据。
    mask = tf.reshape(tf.cast(tf.sequence_mask(length, max_len), tf.float32), tf.shape(inputs))  # 与输入类型相同。
    inputs *= mask
    _sum = tf.reduce_sum(inputs, reduction_indices=-1, keepdims=True) + 1e-9  # keep_dims =True,保持原来的维度和数据。
    return inputs / _sum


with tf.Session() as sess:
    print(sess.run(softmax_with_len(AA, length2, max_len2)))










