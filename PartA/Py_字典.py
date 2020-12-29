#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 27}

print("Value : %s" %  dict.get('Age'))
print("Value : %s" %  dict.get('Sex', "Never"))

# Value : 27
# Value : Never

# 字典的遍历的操作和内容。

a={'a':'1','b':'2','c':'3'}

for key in a.keys():
	print(key+":"+a[key])

print("------------------")

for key in a:
	print(key+":"+a[key])

print("------------------")

for key in a.keys():
    print(key)   # 打印字典的键。

for value in a.values():
    print(value, end=" ")
    				# 打印字典的值。


c:3
a:1
b:2
------------------
c:3
a:1
b:2
------------------
c
a
b
#------------------
2 1 3 # 随机的变化的，不固定。


字典的键必须是唯一的，值不必唯一。

# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。





dict2 = dict(zip([1, 2, 3], [4, 5, 6]))
print(dict2)


{1: 4, 2: 5, 3: 6}



