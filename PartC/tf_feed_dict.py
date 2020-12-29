import numpy as np
import tensorflow as tf
x = tf.placeholder(tf.float32, shape=(4, 4))

y = tf.matmul(x, x)

with tf.Session() as sess:
    rand_array = np.random.rand(4, 4)
    print(sess.run(y, feed_dict={x: rand_array}))  # Will succeed.
