
# 字典的内容，会根据列表的出现的顺序。

list2 = ['B','A','D','C','A']
dict2 = dict.fromkeys(list2,0)

for i in list2:
	dict2[i] += 1

print(dict2)

