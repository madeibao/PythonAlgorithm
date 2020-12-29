from sklearn.metrics import precision_score, recall_score, f1_score
import numpy as np
y_true = np.array([1, 0, 1, 1])
y_pred = np.array([0, 1, 1, 0])

p = precision_score(y_true, y_pred)  #输出结果0.5
r = recall_score(y_true, y_pred)    #输出结果0.333
f1 = f1_score(y_true, y_pred)      #输出0.4

print(p)
print(r)
print(f1)



