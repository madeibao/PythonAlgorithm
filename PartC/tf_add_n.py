import tensorflow as tf
input1 = tf.constant([1.0, 2.0, 3.0])
input2 = tf.Variable(tf.random_uniform([3]))
output = tf.add_n([input1, input2])

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    print(sess.run(input1 + input2))
    print(sess.run(output))



"""


就是一个相加的动作。
[1.8043184 2.081819  3.3279667]
[1.8043184 2.081819  3.3279667]


"""