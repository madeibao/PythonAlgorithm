import tensorflow as tf
x = [[1, 2, 3], [4, 5, 6]]
w = [[7, 8], [9, 10], [11, 12]]
b = [[3, 3], [3, 3]]
result1 = tf.nn.xw_plus_b(x, w, [3, 3])   # 将其封装成一个操作的内容。
result2 = tf.matmul(x, w) + b
init_op = tf.initialize_all_variables()

with tf.Session() as sess:
    # Run the init operation.
    sess.run(init_op)
    print(sess.run(result1))
    print(sess.run(result2))


# ensorflow的设计理念称之为计算流图，在编写程序时，首先构筑整个系统的graph，代码并不会直接生效，
# 这一点和python的其他数值计算库（如Numpy等）不同，graph为静态的，类似于docker中的镜像。然后，在实际的运行时，
# 启动一个session，程序才会真正的运行。这样做的好处就是：避免反复地切换底层程序实际运行的上下文，
# tensorflow帮你优化整个系统的代码。我们知道，很多python程序的底层为C语言或者其他语言，执行一行脚本，
# 就要切换一次，是有成本的，tensorflow通过计算流图的方式，帮你优化整个session需要执行的代码，还是很有优势的。

# 所以placeholder()函数是在神经网络构建graph的时候在模型中的占位，此时并没有把要输入的数据传入模型，
# 它只会分配必要的内存。等建立session，在会话中，运行模型的时候通过feed_dict()函数向占位符喂入数据。


# [[ 61  67]
#  [142 157]]
# [[ 61  67]
#  [142 157]]
