import tensorflow as tf
a = tf.sequence_mask([1, 2, 3], 5)  #一维度的变成二维度的。
b = tf.sequence_mask([[1, 2], [3, 4]])  # 二维度的变成三维度的。

a = tf.cast(a, tf.float32)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(a))
    print(sess.run(b))

"""
[[1. 0. 0. 0. 0.]
 [1. 1. 0. 0. 0.]
 [1. 1. 1. 0. 0.]]

 解析：maxlen是5，所以一共有5列，lengths有三个元素[1,2,3]，所以有三行，每一行分别前1、2、3个元素为True,经过了转型，那么就会变成1或者0.


[[[ True False False False]
  [ True  True False False]]

 [[ True  True  True False]
  [ True  True  True  True]]]

  解析：因为没有指定maxlen，故maxlen默认取lengths中的最大值4，所以一共有4列，lengths是二维数组，
  将其看作由两个一维lengths组成，所以输出也可以看作由这两个一维lengths的输出所组成
"""
