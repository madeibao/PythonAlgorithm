# tf.placeholder(dtype, shape=None, name=None)
# 此函数可以理解为形参，用于定义过程，在执行的时候再赋具体的值。


import tensorflow as tf
import numpy as np

x = tf.placeholder(tf.float32, shape=(10, 10))
y = tf.matmul(x, x)
with tf.Session() as sess:
    rand_array = np.random.rand(10, 10)
    print(sess.run(y, feed_dict={x: rand_array}))  # Will succeed.


# 输出结果为：
"""

[[2.4541163 2.697195  1.2481005 2.3725846 2.7640443 3.0735128 1.991383
  2.9791427 3.5649211 2.2066326]
 [2.4276915 2.069903  1.2488531 2.0668957 2.3069248 2.3986773 1.9513767
  2.634789  3.0070467 2.19405  ]
 [2.266424  3.074651  1.4521759 2.2009563 2.5844889 2.8474307 1.7969754
  2.522596  3.8986566 1.9365711]
 [2.340393  3.0502067 1.7879442 2.353641  2.2758496 2.7921124 1.9031401
  2.2198172 3.485443  2.1180658]
 [1.9018269 1.9875934 1.2356904 1.6260616 1.8543332 1.7207277 1.0749577
  2.2051964 2.6795385 1.4295486]
 [2.4670596 2.2975426 1.2631316 2.4188173 2.2003858 2.827083  1.9982051
  2.6062045 3.021105  1.7346876]
 [2.2155519 1.9533012 1.0282487 2.3836727 2.2190623 2.6337817 1.9970663
  2.946803  2.722618  1.6259322]
 [1.625232  1.7671921 0.8298478 1.5661144 1.9375265 2.2761383 1.6938891
  2.3434248 2.3985567 1.2784824]
 [3.0851762 3.3918738 2.0986338 2.5320907 3.2696097 3.8366606 2.401287
  3.220943  4.4766088 3.0131865]
 [2.3432858 2.000212  1.030254  2.492739  1.7064784 1.9575056 1.8148274
  2.1266155 2.7660608 1.6196928]]
  

"""