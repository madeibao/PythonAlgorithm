import tensorflow as tf

# 初始化矩阵
x = tf.constant([[1., 2., 3.],     # 形状为2*3
                 [1., 2., 3.]])
y = tf.constant([[2., 3., 4.],
                 [2., 3., 4.]])
z = tf.constant([[3., 4.],         # 形状为3*2
                 [3., 4.],
                 [3., 4.]])
# 外积
out = tf.multiply(x, y)
out1 = tf.einsum('ij,ij->ij', x, y)


# 点积
dot = tf.matmul(x, z)
dot1 = tf.einsum('ij,jk->ik', x, z)

# 转置
trans = tf.transpose(x, [1, 0])
trans1 = tf.einsum('ij->ji', x)



with tf.Session() as sess:
    print('外积')
    print('out\n{}'.format(sess.run(out)))
    print('out1\n{}'.format(sess.run(out1)))
    print('点积')
    print('dot\n{}'.format(sess.run(dot)))
    print('dot1\n{}'.format(sess.run(dot1)))
    print('转置')
    print('trans\n{}'.format(sess.run(trans)))
    print('trans1\n{}'.format(sess.run(trans1)))



"""
输出结果为
外积
out
[[ 2.  6. 12.]
 [ 2.  6. 12.]]
out1
[[ 2.  6. 12.]
 [ 2.  6. 12.]]


点积
dot
[[18. 24.]
 [18. 24.]]
dot1
[[18. 24.]
 [18. 24.]]


转置
trans
[[1. 1.]
 [2. 2.]
 [3. 3.]]
trans1
[[1. 1.]
 [2. 2.]
 [3. 3.]]



"""