import tensorflow as tf


X = tf.constant([[1,2,3], [3,2,4]], dtype=tf.float32)     # (2*3)
W = tf.constant([[1,1],[2,2],[3,3]], dtype=tf.float32)    # (3*2)

bias = tf.constant([1, 2], dtype=tf.float32)

sum2 = tf.matmul(X, W)
sum3 = tf.matmul(X, W) + bias


y = tf.nn.softmax(tf.matmul(X, W) + bias)

with tf.Session() as sess:
    print(sess.run(sum2))
    print(sess.run(sum3))
    print(sess.run(y))



# 如果不指定维度的条件下，首先按照的是行进行归一化的操作。
# 默认的是行的归一化的操作，softmax的默认的维度是-1.

    
#  [[14. 14.]
#  [19. 19.]]
# [[15. 16.]
#  [20. 21.]]
# [[0.26894143 0.7310586 ]
#  [0.26894143 0.7310586 ]]



