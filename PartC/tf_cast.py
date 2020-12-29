






import tensorflow as tf
t1 = tf.Variable([1,2,3,4,5])
t2 = tf.cast(t1,dtype=tf.float32)
print('t1: {}'.format(t1))
print('t2: {}'.format(t2))
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(t2)
    print(t2.eval())
    # print(sess.run(t2))

    # 输出结果为 [1. 2. 3. 4. 5.]

