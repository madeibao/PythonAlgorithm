import tensorflow as tf
import numpy as np


def softmax(x):
    sum_raw = np.sum(np.exp(x), axis=-1)
    x1 = np.ones(np.shape(x))
    for i in range(np.shape(x)[0]):
        x1[i] = np.exp(x[i]) / sum_raw[i]
    return x1


y = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0]])  # 每一行只有一个1
logits = np.array([[12, 3, 2], [3, 10, 1], [1, 2, 5], [4, 6.5, 1.2], [3, 6, 1]])
y_pred = softmax(logits)
print(y_pred)


E1 = -np.sum(y * np.log(y_pred), -1)

sess = tf.Session()
y = np.array(y).astype(np.float64)
E2 = sess.run(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=logits))
print('按计算公式计算的结果:\n', E1)  # 按计算公式计算的结果
print('tf计算的结果:\n', E2)




# 输出的E1，E2结果相同
# 这里是交叉熵的损失函数。
# 结果为：
# 按计算公式计算的结果:
#  [1.68795487e-04 1.03475622e-03 6.58839038e-02 2.58349207e+00
#  5.49852354e-02]
# tf计算的结果:
#  [1.68795487e-04 1.03475622e-03 6.58839038e-02 2.58349207e+00
#  5.49852354e-02]