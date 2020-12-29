

# 用函数实现十进制与二进制的转换


def tenTotwo(number):
    #定义栈
    s = []
    binstring = ''
    while number > 0:
        #余数进栈
        rem = number % 2
        s.append(rem)
        number = number // 2
    while len(s) > 0:
        #元素全部出栈即为所求二进制数
        binstring = binstring + str(s.pop())
    print(binstring)

#实例
tenTotwo(233)


