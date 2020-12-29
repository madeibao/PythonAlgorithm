import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


state = tf.Variable(1)
state_ = tf.assign(state, 10)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(state))
    print(sess.run(state_))
    print(sess.run(state))


# 1
# 10
# 10
