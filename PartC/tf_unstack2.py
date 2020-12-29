import tensorflow as tf
import numpy as np

t = np.random.randint(1, 10, (3, 5))   # 一个三行五列的数据，并且数据的范围是1到10之间。
ustack1 = tf.unstack(t, axis=1)        # 按照纵行进行切分。
ustack2 = tf.unstack(t, axis=0)        # 按照横行进行切分。
sess = tf.Session()
print(t)
print(sess.run(ustack1))
print(sess.run(ustack2))



# [[8 6 4 3 5]
#  [6 2 5 8 4]
#  [9 5 9 6 9]]
# [array([8, 6, 9]), array([6, 2, 5]), array([4, 5, 9]), array([3, 8, 6]), array([5, 4, 9])]
# [array([8, 6, 4, 3, 5]), array([6, 2, 5, 8, 4]), array([9, 5, 9, 6, 9])]
