import tensorflow as tf
import numpy as np

A = list([1, 2, 3])
B = np.array([1, 2, 3])
C = tf.convert_to_tensor(A)   # 把任何的内容都可以变成张量的形式来进行存储。
D = tf.convert_to_tensor(B)

with tf.Session() as sess:
    print(type(A))
    print(type(B))
    print(type(C))
    print(type(D))
    print(sess.run(C))
    print(sess.run(D))



'''
<class 'numpy.ndarray'>
<class 'tensorflow.python.framework.ops.Tensor'>
<class 'tensorflow.python.framework.ops.Tensor'>
[1 2 3]
[1 2 3]

'''


