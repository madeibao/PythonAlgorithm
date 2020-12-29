"""
tensorboard 的简单使用---查看图的结构
"""
import tensorflow as tf
# 清除default graph 和不断增加的节点
tf.reset_default_graph()
# Logdir为自己机器上的合适路径

logdir = 'E:/D/TF_Log'			# 设置一个路径用来进行存储张量图，自己设置就好。

# 定义一个简单的计算图,实现向量加法的操作
input1 = tf.constant([1.0, 2.0, 3.0], name='input1')
input2 = tf.Variable(tf.random_uniform([3]), name='input2')
output = tf.add_n([input1, input2], name='add')
# 生成一个写日志的writer,并将当前的TensorFlow计算图写入日志
writer = tf.summary.FileWriter(logdir, tf.get_default_graph())
writer.close()






通过cmd的命令，窗口命令进入到logdir的目录之内。
tensorboard --logdir=E:/D/TF_Log --host=127.0.0.1
然后会产生一个引用，
在谷歌浏览器里面输入http://127.0.0.1:6006
然后就可以看到结果





