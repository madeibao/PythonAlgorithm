# 实际上tf.nn.embedding_lookup的作用就是找到要寻找的embedding data中的对应的行下的vector。




import tensorflow as tf
import numpy as np
c = np.random.random([5, 1])     			  #  #随机生成一个5*1的数组
b = tf.nn.embedding_lookup(c, [1, 3])  		  #  #查找数组中的序号为1和3的


with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())   # 通用的写法，全局的初始化。
    print(sess.run(b))
    print(c)




"""
	输出结果为：
	[[0.65521926]
	 [0.91452257]]
	 
	[[0.12151747]
	 [0.65521926]
	 [0.1518894 ]
	 [0.91452257]
	 [0.66205948]]


"""