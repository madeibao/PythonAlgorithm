
import tensorflow as tf
# 两个矩阵对应元素各自相乘
x = tf.constant([[1., 2., 3.],
                 [1., 5., 3.],
                 [1., 2., 9.]])

x1 = tf.reduce_sum(x)
x2 = tf.reduce_sum(x, 0)  # 第零维度的统计之和。
x3 = tf.reduce_sum(x, reduction_indices=1)  # 指针表示1和-1的，效果是一样的。
x6 = tf.reduce_sum(x, reduction_indices=-1)
x4 = tf.reduce_sum(x, reduction_indices=[1, 0])  # 这种得出的是最终的一个数字,先统计一维度，然后是零维度的。
x5 = tf.reduce_sum(x, reduction_indices=[0, 1])  # 这种得出的是要给数字，和上面的是一个效果。

with tf.Session() as sess:
    print(sess.run(x1))
    print(sess.run(x2))
    print(sess.run(x3))
    print(sess.run(x4))
    print(sess.run(x5))
    print(sess.run(x6))

"""
27.0
[ 3.  9. 15.]
[ 6.  9. 12.]
[ 6.  9. 12.]
27.0
27.0


"""




