"""
用来显示标量信息，其格式为：

tf.summary.scalar(tags, values, collections=None, name=None)
例如：tf.summary.scalar('mean', mean)

一般在画loss,accuary时会用到这个函数。
"""

import tensorflow as tf
g1 = tf.Graph()
 
with g1.as_default():
    sess = tf.Session()
    a = tf.constant(5, name="a")
    b = tf.constant(5, name="b")
    c = tf.add(a, b, "add_in_g1")
    tf.summary.scalar("c", c)
    merged_summary = tf.summary.merge_all()
    writer = tf.summary.FileWriter("E:/pythonWorkSpace/YLog", sess.graph) # 启动张量运算，然后存储，可以观察后来的结果。
    summary = sess.run(merged_summary)
    writer.add_summary(summary=summary, global_step=1)
    writer.close()
    print(sess.run(c))
    sess.close()


