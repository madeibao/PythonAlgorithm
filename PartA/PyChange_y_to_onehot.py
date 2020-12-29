
y = [1,1,1,1,1,0,1,0,1,0,1,0,0,0,1,-1,0,0,-1,-1,-1,-1,-1]


def change_y_to_onehot(y):      # 转变成y_onehot向量。
    from collections import Counter
    print(Counter(y))           # 统计出现的次数。

    class_set = set(y)          # 建立一个类别，   (0,1,-1)   集合不重复的元素，所以一共有三种类别。
    n_class = len(class_set)    # 最终建立了三个类别的数据。  n_class = 3


    y_onehot_mapping = dict(zip(class_set, range(n_class)))   #  {0: 0, 1: 1, -1: 2}  建立了一个一一对应的关系。

    onehot = []
    for label in y:
        tmp = [0] * n_class
        tmp[y_onehot_mapping[label]] = 1
        onehot.append(tmp)

    return np.asarray(onehot, dtype=np.int32)


print(change_y_to_onehot(y))


"""
[[0 1 0]
 [0 1 0]
 [0 1 0]
 [0 1 0]
 [0 1 0]
 [1 0 0]
 [0 1 0]
 [1 0 0]
 [0 1 0]
 [1 0 0]
 [0 1 0]
 [1 0 0]
 [1 0 0]
 [1 0 0]
 [0 1 0]
 [0 0 1]
 [1 0 0]
 [1 0 0]
 [0 0 1]
 [0 0 1]
 [0 0 1]
 [0 0 1]
 [0 0 1]]

"""
