1.保存
将训练好的模型参数保存起来，以便以后进行验证或测试。tf里面提供模型保存的是tf.train.Saver()模块。
模型保存，先要创建一个Saver对象：如
saver=tf.train.Saver()
在创建这个Saver对象的时候，有一个参数经常会用到，max_to_keep 参数，这个是用来设置保存模型的个数，默认为5，即 max_to_keep=5，保存最近的5个模型。
如果想每训练一代(epoch)就想保存一次模型，则可以将 max_to_keep设置为None或者0，但是这样做除了多占用硬盘，并没有实际多大的用处，因此不推荐，如：
saver=tf.train.Saver(max_to_keep=0)
当然，如果你只想保存最后一代的模型，则只需要将max_to_keep设置为1即可，即
saver=tf.train.Saver(max_to_keep=1)
创建完saver对象后，就可以保存训练好的模型了，如：
saver.save(sess,'ckpt/mnist.ckpt',global_step=step)


第二个参数设定保存的路径和名字，第三个参数将训练的次数作为后缀加入到模型名字中。
saver.save(sess, 'my-model', global_step=0) ==> filename: 'my-model-0'
...
saver.save(sess, 'my-model', global_step=1000) ==> filename: 'my-model-1000'




