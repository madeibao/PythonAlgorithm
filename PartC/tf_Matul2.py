
import tensorflow as tf

x3 = tf.constant([[1., 2., 3.],
                  [1., 2., 3.]], dtype=tf.float32)  # 2*3

y3 = tf.constant([[3, 3],
                  [3, 2],
                  [2, 4]], dtype=tf.float32)   	    # 3*2

z2 = tf.matmul(x3, y3)
with tf.Session() as sess:
    print(sess.run(z2))

    # 两个维度的计算。至少要求第二个维度要相同.

"""

[[15. 19.]
 [15. 19.]]

"""

