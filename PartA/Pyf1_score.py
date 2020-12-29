from sklearn.metrics import f1_score

y_true = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4]
y_pred = [1, 1, 1, 0, 0, 2, 2, 3, 3, 3, 4, 3, 4, 3]
print(f1_score(y_true, y_pred, labels=[1, 2, 3, 4], average='micro'))
# 输出结果为：0.6153846153846153




"""

'macro':Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account.
'macro':分布计算每个类别的F1，然后做平均（各类别F1的权重相同）

"""