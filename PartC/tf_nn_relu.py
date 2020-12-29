



# # 非线性的激活函数内容。
# 						   /
# 						  /
# 					     /
# 					    /
# _____________________/
# 只要<0 的结果，全部变成0




import tensorflow as tf

input_data = tf.constant([[0, 10, -10], [-1, 2, -3], [1, 1.2, 3.3]], dtype=tf.float32)
output = tf.nn.relu(input_data)
sess = tf.Session()

print(sess.run(output))




# [[ 0.  10.   0. ]
#  [ 0.   2.   0. ]
#  [ 1.   1.2  3.3]]
