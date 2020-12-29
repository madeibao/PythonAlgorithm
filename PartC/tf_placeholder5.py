

import tensorflow as tf
import numpy as np

x = tf.placeholder(tf.float32, [1, None])  # 这里表示的是第一个维度的数据是未知的，具体的启动时再确定。

with tf.Session() as sess:
    xs = np.random.rand(1, 5)
    print(sess.run(x, feed_dict={x: xs}))



# 这里表示出是要给行向量。

# [[0.5844027  0.83865994 0.26693517 0.9312852  0.8528017 ]]