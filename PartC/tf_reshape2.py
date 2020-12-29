

import tensorflow as tf
a = tf.constant([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6])
a = tf.reshape(a, [3, 2, 3])
b = tf.reshape(a, [-1, 2, 3])
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(a))
    print(sess.run(b))



"""


[[[1 1 1]
  [2 2 2]]

 [[3 3 3]
  [4 4 4]]

 [[5 5 5]
  [6 6 6]]]

  
[[[1 1 1]
  [2 2 2]]

 [[3 3 3]
  [4 4 4]]

 [[5 5 5]
  [6 6 6]]]

  当不知道维度的时候，可以通过利用-1来代替，然后自动的计算出结果。
"""