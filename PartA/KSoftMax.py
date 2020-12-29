from keras import backend as K
import tensorflow as tf

x2 = K.constant([[1, 1, 1, 1],
                 [2, 2, 2, 2],
                 [2, 3, 5, 8]], dtype=tf.float32)

temp = K.softmax(x2)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(temp))

# [[0.25       0.25       0.25       0.25      ]
#  [0.25       0.25       0.25       0.25      ]
#  [0.00234065 0.00636253 0.04701312 0.9442838 ]]






