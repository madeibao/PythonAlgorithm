import tensorflow as tf

t = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9,])

x3 = tf.constant([[1., 2., 3.],
                  [1., 5., 3.],
                  [1., 2., 3.]])

out =tf.reshape(x3, [-1])  # 展平的操作， 就是变成一行。
t2 = tf.reshape(t, [3, 3])
t3 = tf.reshape(t, [9, -1])
t4 = tf.reshape(t, [-1, 9])


with tf.Session() as sess:
    print(sess.run(t2))
    print(sess.run(t3))
    print(sess.run(t4))
    print(sess.run(out))


"""
输出结果为：

[[1 2 3]
 [4 5 6]
 [7 8 9]]

[[1]
 [2]
 [3]
 [4]
 [5]
 [6]
 [7]
 [8]
 [9]]
 
[[1 2 3 4 5 6 7 8 9]]

[1. 2. 3. 1. 5. 3. 1. 2. 3.]


"""