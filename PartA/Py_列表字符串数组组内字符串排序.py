



comID = ["abcd", "zesa", "saze", "abc", "pqrst", "cdab", "bacd"]
list1 = [] 

for i in range(len(comID)):
	list1.append(''.join(sorted(list(comID[i]))))

print(list1)


# 字符串数组的组內部的元素进行排序。

# ['abcd', 'aesz', 'aesz', 'abc', 'pqrst', 'abcd', 'abcd']



# 列表的字符串进行排序。
#---------------------------------------------------------------
comID = ["abcd", "zesa", "saze", "abc", "pqrst", "cdab", "bacd"]
list2 = sorted(comID)
print(list2)



['abc', 'abcd', 'bacd', 'cdab', 'pqrst', 'saze', 'zesa']
















