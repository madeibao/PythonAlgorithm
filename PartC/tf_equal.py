

import tensorflow as tf
x = [1, 3, 0, 2]
y = [1, 4, 2, 2]
equal = tf.equal(x, y)
with tf.Session() as sess:
    print(sess.run(equal))


"""
[ True False False  True]  
首先，返回的是布尔类型。

"""



