
from collections import Counter


"""
	把列表变成字典的形式进行存储。
"""
word2id = {}
a = ['你好', '你好', '中国', '华为', '荣耀']
b = Counter(a).most_common()

for word, _ in b:
    word2id[word] = len(word2id)

print(word2id)


"""
{'华为': 1, '你好': 0, '荣耀': 2, '中国': 3}

"""


