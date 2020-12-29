import tensorflow as tf

# 't' is a tensor of shape [2]
t = tf.constant([1, 2])
me = tf.constant([[1, 2, 3],
                  [3, 4, 4]])

t3 = tf.expand_dims(me, 2)
with tf.Session() as sess:
    print(sess.run(t3))
    print(sess.run(tf.shape(me)))  # 注意观察维度和数据
    print(sess.run(tf.shape(t3)))




# [[[1]
#   [2]
#   [3]]

#  [[3]
#   [4]
#   [4]]]


# [2 3]
# [2 3 1]




