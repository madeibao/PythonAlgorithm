



python中的dict是无序的，默认的是hashmap的存储
python中的collections有一个模块是排序字典。 OrderedDict()


import collections
dd = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
#按key排序
kd = collections.OrderedDict(sorted(dd.items(), key=lambda t: t[0]))
print(kd)

#按照value排序
vd = collections.OrderedDict(sorted(dd.items(),key=lambda t:t[1]))
print(vd)


#输出
OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])



# ------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------
# 排序字典



from collections import OrderedDict
list2 = [3,2,3,4,2,4,9,10,6,6,7,9,9]

dict2 = OrderedDict()
for c in list2:
    dict2[c] = dict2[c] +1 if c in dict2 else 1

print(dict2)


# 首先按照的是列表中，可迭代对象中的数字来进行排序。
OrderedDict([(3, 2), (2, 2), (4, 2), (9, 3), (10, 1), (6, 2), (7, 1)])


