

import tensorflow as tf
value = [[1, 2, 3, 4],
         [4, 5, 6, 8],
         [9, 10, 11, 12]]

value2 = [[1, 2, 3],
          [4, 5, 6]]
split0, split1 = tf.split(value, [1, 2], 0)
# axis=0 代表的是按照行划分，同理，axis=1 代表的是按照列划分。  默认的情况下是按照行分割。
split3, split4, split5 = tf.split(value2, [1, 2, 0], 1)

with tf.Session() as sess:
    print(sess.run(split0))
    print(sess.run(split1))
    print(sess.run(split3))
    print(sess.run(split4))
    print(sess.run(split5))


"""
#结果：

[[1 2 3 4]]
[[ 4  5  6  8]
 [ 9 10 11 12]]
[[1]
 [4]]
[[2 3]
 [5 6]]
[]

"""