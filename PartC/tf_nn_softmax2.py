





import tensorflow as tf

input_data = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.float32)
with tf.Session() as sess:
    print(sess.run(tf.nn.softmax(input_data, axis=0)))




当axis=0 的时候，进行的归一化如下

1 2 3 
4 5 6
7 8 9

每一列的元素内容来进行归一化的操作。

[[0.00235563 0.00235563 0.00235563]
 [0.04731416 0.04731416 0.04731416]
 [0.95033026 0.95033026 0.95033026]]


当axis= 1 的时候，进行的是行的归一化的操作内容

[[0.09003057 0.24472848 0.66524094]
 [0.09003057 0.24472848 0.66524094]
 [0.09003057 0.24472848 0.66524094]]




 tensorflow的默认的是按照行的方式来进行归一化的操作，默认的是行的归一化。


 