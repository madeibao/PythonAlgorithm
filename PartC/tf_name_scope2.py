
# 也就是说，它的主要目的是为了更加方便地管理参数命名。
# 与 tf.Variable() 结合使用。简化了命名
with tf.name_scope('conv1') as scope:
    weights1 = tf.Variable([1.0, 2.0], name='weights')
    bias1 = tf.Variable([0.3], name='bias')

# 下面是在另外一个命名空间来定义变量的
with tf.name_scope('conv2') as scope:
    weights2 = tf.Variable([4.0, 2.0], name='weights')
    bias2 = tf.Variable([0.33], name='bias')

# 所以，实际上weights1 和 weights2 这两个引用名指向了不同的空间，不会冲突
print(weights1.name)
print(weights2.name)


#-------------------------------------------------------------------
主要与tf.Variable搭配使用；
当传入字符串时，用以给变量名添加前缀，类似于目录，如case1所示；
当传入已存在的name_scope对象时，则其范围内变量的前缀只与当前传入的对象有关，与更上层的name_scope无关，如case2所示。



import tensorflow as tf

# case 1:

with tf.name_scope('l1'):
    with tf.name_scope('l2'):
        wgt1 = tf.Variable([1, 2, 3], name='wgts')
        bias1 = tf.Variable([0.1], name='biases')

print(wgt1.name, bias1.name)

# >>> l1/l2/wgts:0 l1/l2/biases:0

# case 2:

with tf.name_scope('l1') as l1_scp:
    with tf.name_scope('l2'):
        wgt0 = tf.Variable([1, 2, 3], name='wgts')

        bias0 = tf.Variable([0.1], name='biases')

        with tf.name_scope(l1_scp):
            wgt1 = tf.Variable([1, 2, 3], name='wgts')

            bias1 = tf.Variable([0.1], name='biases')

print(wgt0.name, bias0.name, wgt1.name, bias1.name)

# >>> l1_1/l2/wgts:0 l1_1/l2/biases:0 l1_1/wgts:0 l1_1/biases:0