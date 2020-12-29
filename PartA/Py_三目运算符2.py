



x = int(input("please enter first integer:"))
y = int(input("please enter second integer:"))

# 一般的写法
if x == y:
    print("两数相同！")
elif x > y:
    print("较大的数为：", x)
else:
    print("较大的数为：", y)







# 三目运算符写法
print(x if (x > y) else y)









