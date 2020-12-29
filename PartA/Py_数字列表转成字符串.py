

list1 = [1, 2, 3, 4, 5, 6]

print("".join(str(i) for i in list1))


# 123456

# 输出结果为123456




字符串数字转化成数字列表

str1 = "123456"

list1 = []
for i in range(len(str1)):
    list1.append(int(i))
print(list1)


[0, 1, 2, 3, 4, 5]
num = [1, 2, 3, 4, 5]
str2 = list(map(str,num))


print(str2)

['1','2','3','4','5']





