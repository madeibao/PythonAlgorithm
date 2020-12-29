"""
格式：tf.summary.merge(inputs, collections=None, name=None)
一般选择要保存的信息还需要用到tf.get_collection()函数




使用tf.get_collection函数筛选图中summary信息中的accuracy信息，这里的
 tf.GraphKeys.SUMMARIES  是summary在collection中的标志。

"""



tf.summary.scalar('accuracy',acc)                   #生成准确率标量图  
merge_summary = tf.summary.merge([tf.get_collection(tf.GraphKeys.SUMMARIES,'accuracy'),...(其他要显示的信息)])  

train_writer = tf.summary.FileWriter(dir,sess.graph)#定义一个写入summary的目标文件，dir为写入文件地址  

......(交叉熵、优化器等定义)  

for step in range(training_step):                  #训练循环  

    train_summary = sess.run(merge_summary,feed_dict =  {...})#调用sess.run运行图，生成一步的训练过程数据  

    train_writer.add_summary(train_summary,step)#调用train_writer的add_summary方法将训练过程以及训练步数保存  





