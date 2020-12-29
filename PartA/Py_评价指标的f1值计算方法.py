




from sklearn.metrics import f1_score

y_pred = [0, 1, 1, 1, 2, 2]
y_true = [0, 1, 0, 2, 1, 1]
print(f1_score(y_true, y_pred, average='macro'))
print(f1_score(y_true, y_pred, average='weighted'))









