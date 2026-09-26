
from collections import Counter
# 字典的内容，会根据列表的出现的顺序。

list2 = ['B','A','D','C','A']
dict2 = dict.fromkeys(list2,0)

for i in list2:
	dict2[i] += 1

print(dict2)

print('-------------------')
list3 = ['B','A','D','C','A']
# 直接使用Counter来统计列表中元素的出现次数
dict3 = Counter(list3) 
print(dict3)