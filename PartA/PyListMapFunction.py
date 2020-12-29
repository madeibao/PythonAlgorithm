

dict = {b'tuna': 74, b'in': 16, b'.': 27, b'the': 70, b'try': 63, b'people': 67,
        b'straight-forward': 20, b'disappoints': 68, b'roll': 1, b'rose': 51, b'delivery': 57, }   # 这里是一个字典的创建。

target_word = ['tuna', b'in']   # 必须是一个列表的形式来存储。
target_word = list(map(lambda w: dict.get(w, 0), target_word))

print(target_word)


# 结果为：
# [74, 16]
# 如果列表之内的元素不存在，就会返回0这个结果。
# [0, 0]







