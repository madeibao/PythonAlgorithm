import tensorflow as tf

# 't' is a tensor of shape [2]
t = tf.constant([1, 2])
me = tf.constant([[1, 2], 
                  [3, 4]])

t1 = tf.expand_dims(t, -1)
t2 = tf.expand_dims(t, 0)
t3 = tf.expand_dims(t, 1)
t4 = tf.expand_dims(me, 2)


with tf.Session() as sess:
    print(sess.run(t))
    print("\n")
    print(sess.run(t1))
    print("\n")
    print(sess.run(t2))
    print("\n")
    print(sess.run(t3))
    print(sess.run(t4))



"""
输出结果为
[1 2]


[[1]
 [2]]


[[1 2]]


[[1]
 [2]]

 
[[[1]
  [2]]

 [[3]
  [4]]]


"""