
import tensorflow as tf

a = tf.constant([[1, 2, 3, 4, ], [5, 6, 7, 8, ], [9, 10, 11, 12, ], [13, 14, 15, 16]])
l = tf.constant([1, 2, 3, 4], tf.int64)   # 每一次翻转长度分别为1,2,3.由于a是（3,3）维的，所以l中数值最大只能是3
x = tf.reverse_sequence(a, seq_lengths=l, seq_axis=0, batch_axis=1)   # 以列为单位进行翻转，翻转的是每一行的元素
y = tf.reverse_sequence(a, seq_lengths=l, seq_axis=1, batch_axis=0)   # 以行为单位进行翻转，翻转的是每一列的元素
with tf.Session() as sess:
    print(sess.run(x))
    print(sess.run(y))




"""

1 	2	3	4
5	6	7	8
9	10	11	12
13	14	15	16


反转的操作如下：
 [ 1  6 11 16]
 [ 5  2  7 12]
 [ 9 10  3  8]
 [13 14 15  4]

依照列为单位反转的是每一行的元素，所以
第一列，1反转，还是1，
第二列，6与2反转，结果为：
						2  6
						6  2

第三列，  3  11
		 7   7
		11   3

第四列做出镜像的反转，
		4     16
		8     12
		12    8
		16	  4

"""