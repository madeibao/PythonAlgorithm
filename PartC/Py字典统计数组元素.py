

list2 = [2, 3, 4, 2, 3, 4, 3, 2, 3, 4, 5, 6, 7, 9, 10]
dict2 = {}



for i in list2:
    dict2[i] = dict2.get(i, 0) + 1


for key in dict2:
    print(str(key)+" "+str(dict2[key]))



# 一个字典统计列表中的元素的出现的次数。

