import tensorflow as tf
X = tf.constant([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=tf.float32)

tan = tf.nn.tanh(X)
with tf.Session() as sess:
    print(sess.run(tan))




# 当x趋向于无穷的时候，所以，tanh(x)的值趋向于1.
# 线性的激活函数
"""
[0.7615942  0.9640276  0.9950547  0.9993292  0.99990916 0.99998784
 0.99999833 0.99999976 1.         1.        ]

自己构建tanh函数。


import tensorflow as tf
X1 = tf.constant(10, dtype=tf.float32)
X2 = tf.constant(-10, dtype=tf.float32)

x1 = tf.exp(X1)
x2 = tf.exp(X2)
temp = (x1-x2)/(x1+x2)
tan = tf.nn.tanh(X1)
with tf.Session() as sess:
    print(sess.run(tan))
    print(sess.run(temp))


输出结果为
1.0
1.0

"""