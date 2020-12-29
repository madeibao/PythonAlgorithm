

import tensorflow as tf
import matplotlib.pyplot as plt

tn = tf.truncated_normal([20], mean=5, stddev=1)

sess = tf.Session()
ov = sess.run(tn)
print(ov)
plt.plot(ov)
plt.show()





# [6.514302  5.6332736 5.6107883 5.07814   4.3867226 3.5002818 4.949364
#  6.091163  4.4551363 4.695559  5.3525257 6.158372  4.5669017 6.394979
#  3.7713776 5.1239085 5.766552  6.0900564 4.454388  5.827808 ]
