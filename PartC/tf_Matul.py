
import tensorflow as tf

# 两个矩阵对应元素各自相乘

x=tf.constant([[1., 2., 3.],
               [1., 2., 3.],
               [1., 2., 3.]])
y=tf.constant([[0., 0., 1.],
               [0., 0., 1.],
               [0., 0., 1.]])


# 注意这里x,y必须要有相同的数据类型，不然就会因为数据类型不匹配报错
z=tf.multiply(x,y)

# 两个数相乘
x1 = tf.constant(1)
y1 = tf.constant(2)
# 注意这里x,y必须要有相同的数据类型，不然就会因为数据类型不匹配报错
z1=tf.multiply(x1,y1)

#数和矩阵相乘
x2=tf.constant([[1., 2., 3.],
                [1., 2., 3.],
                [1., 2., 3.]])
y2=tf.constant(2.0)
# 注意这里x,y必须要有相同的数据类型，不然就会因为数据类型不匹配报错
z2=tf.multiply(x2, y2)

# 两个矩阵相乘
x3 = tf.constant([[1.,2.,3.],
                  [1.,2.,3.],
                  [1.,2.,3.]])

y3 = tf.constant([[0.,0.,1.],
                  [0.,0.,1.],
                  [0.,0.,1.]])

# 注意这里x，y要满足矩阵相乘的格式要求
z3=tf.matmul(x3,y3)

with tf.Session() as sess:
    print(sess.run(z))
    print(sess.run(z1))
    print(sess.run(z2))
    print(sess.run(z3))


"""

[[0. 0. 3.]
 [0. 0. 3.]
 [0. 0. 3.]]

2

[[2. 4. 6.]
 [2. 4. 6.]
 [2. 4. 6.]]


[[0. 0. 6.]
 [0. 0. 6.]
 [0. 0. 6.]]


"""