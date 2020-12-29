import tensorflow as tf
import numpy as np

x = tf.placeholder(tf.float32, [None, 3])  # 这里表示的是第一个维度的数据是未知的，具体的启动时再确定。

with tf.Session() as sess:
    xs = np.random.rand(10, 3)
    print(sess.run(x, feed_dict={x: xs}))


# [[0.21493666 0.6431164  0.56490016]
#  [0.39895493 0.10703538 0.12280177]
#  [0.57571405 0.2968762  0.7782009 ]
#  [0.5134823  0.20911594 0.9510833 ]
#  [0.375885   0.80928844 0.06618588]]
