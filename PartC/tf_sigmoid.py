import tensorflow as tf

a = tf.constant([[1.0, 2.0], [1.0, 2.0], [1.0, 2.0]])
sess = tf.Session()
print(sess.run(tf.sigmoid(a)))




# [[0.7310586 0.880797 ]
#  [0.7310586 0.880797 ]
#  [0.7310586 0.880797 ]]



# tf.sigmoid(a) = 1/(1 + exp (-a))。



