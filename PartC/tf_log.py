import tensorflow as tf

# 定义‘符号’变量，也称为占位符

a = tf.placeholder("float")
y = tf.log(a)  # 构造一个op节点
with tf.Session() as sess:
	print(sess.run(y, feed_dict={a: 2.718281828459045}))
	sess.close()

# 计算依照自然对数为底的对数值
# 结果为1.0

