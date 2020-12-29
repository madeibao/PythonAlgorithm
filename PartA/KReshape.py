from keras import backend as K
import tensorflow as tf

x2 = K.constant([[1, 1, 1, 1],
                 [2, 2, 2, 2],
                 [2, 3, 5, 8]], dtype=tf.float32)

temp = K.reshape(x2, (-1,6))

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(temp))



# [[1. 1. 1. 1. 2. 2.]
#  [2. 2. 2. 3. 5. 8.]]





