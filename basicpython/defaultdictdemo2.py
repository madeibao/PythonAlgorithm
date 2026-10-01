
from collections import defaultdict

# 参数是一个"工厂函数"，用来生成默认值
d = defaultdict(list)
d['a'].append(1)   # 'a' 不存在，自动创建为 []
d['a'].append(2)
d['b'].append(3)
print(d)  # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})

print(d['c'])  # 'c' 不存在，自动创建为 []，输出 []
print(d['a'])  # 输出 [1, 2]


