
import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()  # 控制条件成立。

w = tf.get_variable("w", shape=[2, 4])
print(w.numpy())




# 结果能够立即的执行。


# [[-0.7471616  -0.5936618  -0.4333005   0.88156414]
#  [-0.64015007 -0.06995225  0.622493    0.89952254]]





