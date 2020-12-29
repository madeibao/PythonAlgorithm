
import tensorflow as tf
# 元素类型可以看到第一个值value是必须的，可以是一个数值，也可以是一个列表。
tensor = tf.constant([1, 2], dtype=tf.float32)
with tf.Session() as sess:
    print(sess.run(tensor))

    












    