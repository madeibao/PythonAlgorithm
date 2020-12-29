
import tensorflow as tf

# 两个矩阵对应元素各自相乘
# 输入的向量，输出的结果对应也是向量的表示形式。

x3 = tf.constant([[1., 2., 3.],
                  [1., 5., 3.],
                  [1., 2., 3.]])
inputs = tf.exp(x3)
with tf.Session() as sess:
    print(sess.run(inputs))


'''
[[  2.7182817   7.389056   20.085537 ]
 [  2.7182817 148.41316    20.085537 ]
 [  2.7182817   7.389056   20.085537 ]]

'''