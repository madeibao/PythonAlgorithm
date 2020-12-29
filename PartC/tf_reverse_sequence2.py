import tensorflow as tf

a = tf.constant([[1, 2, 3],
                 [1, 2, 3],
                 [1, 2, 3]])
l = tf.constant([2, 3, 3], tf.int64)
b = tf.reverse_sequence(a, seq_lengths=l, batch_axis=0, seq_axis=1)

c = tf.Print(b, [b], summarize=9)  # 通过内容在一行之内进行显示.
with tf.Session() as sess:
    print(sess.run(b))
    sess.run(c)




# 显示结果为如图所示。
# [[2 1 3]
#  [3 2 1]
#  [3 2 1]]
# 
# [[2 1 3][3 2 1][3 2 1]]


