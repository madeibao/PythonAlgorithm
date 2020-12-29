
import tensorflow as tf
x = tf.placeholder(tf.int32, [None, 4])   #首先没有声明行的内容，
with tf.Session() as sess:
    print(sess.run(x, feed_dict={x: [[1, 2, 3, 4], [2, 3, 4, 5]]}))  # 具体的时候再喂养给数据


# [[1 2 3 4]
#  [2 3 4 5]]