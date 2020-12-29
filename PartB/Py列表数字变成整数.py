

a= [1, 2, 3, 4]


# 方法1用数学方法计算出结果
num = functools.reduce(lambda x, y: x*10+y, a)
print(num)  # 1234

# 方法2用字符串合并出结果
print(int(functools.reduce(lambda x, y: str(x)+str(y), a)))

# 1234



# 分解数字变成列表存储.

num2 = 123
str2 = str(num2)
list2 = [int(i) for i in str2]
print(list2)

