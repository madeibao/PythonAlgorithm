
import tensorflow as tf

a = tf.constant([1., 2., 3., 0., 9., ])
b = tf.constant([[1, 2, 3],
                 [3, 2, 1],
                 [4, 5, 6],
                 [6, 5, 4]])

with tf.Session() as sess:
    print(sess.run(tf.argmax(a, dimension=0)))
    print(sess.run(tf.argmax(b, dimension=0)))  # 注意dimension可以省略掉,直接的写出即可.(a, 0)
    print(sess.run(tf.argmax(b, dimension=1)))



"""

dimension=0 按列找 
dimension=1 按行找 
tf.argmax()返回最大数值的下标 



4
[3 2 2]
[2 0 2 0]


"""



