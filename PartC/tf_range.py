import tensorflow as tf
# 从0开始计数。
x = tf.range(8.0, 13.0, 2.0)
y = tf.range(10, 15)
z = tf.range(3, 1, -0.5)
w = tf.range(3)
m = tf.range(0, 10)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(x))#输出[  8.  10.  12.]
    print(sess.run(y))#输出[10 11 12 13 14]
    print(sess.run(z))#输出[ 3.   2.5  2.   1.5]
    print(sess.run(w))#输出[0 1 2]sess = tf.Session()
    print(sess.run(m))





"""
[ 8. 10. 12.]
[10 11 12 13 14]
[3.  2.5 2.  1.5]
[0 1 2]
[0 1 2 3 4 5 6 7 8 9]

"""