


'''
tf.placeholder(
    dtype,
    shape=None,
    name=None)
'''
# 参数：
# dtype：数据类型。常用的是tf.float32,tf.float64等数值类型
# shape：数据形状。默认是None，就是一维值，也可以是多维（比如[2,3], [None, 3]表示列是3，行不定）
# name：名称



import tensorflow as tf
import numpy as np

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

with tf.Session() as sess:

    print(sess.run(output, feed_dict = {input1:[3.], input2: [4.]}))
