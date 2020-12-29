



import tensorflow as tf
A = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
with tf.Session() as sess:
        print(sess.run(tf.nn.softmax(A)))


# 输出结果为：[0.00426978 0.01160646 0.03154963 0.08576079 0.233122   0.6336913 ]






















