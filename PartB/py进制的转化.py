

#Python3 实例--Python 十进制转二进制、八进制、十六进制：
print("Python3 实例--Python 十进制转二进制、八进制、十六进制：")
#原则：如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。

def jinzhi_change(x):
    print("{}的二进制值为：{}".format(x, bin(x)))
    print("{}的八进制值为：{}".format(x, oct(x)))
    print("{}的十六进制值为：{}".format(x, hex(x)))

jinzhi_change(int(input()))
#================================================================================================
# 十进制变成二进制的形式


def Dec2Bin(dec):
    # 递归
    result = ''
    if dec:
        result = Dec2Bin(dec // 2)
        return result + str(dec % 2)
    else:
        return result

print(Dec2Bin(10))

#================================--------------------------------------------------------------------------------------------------------------------
# 非递归的写法，十进制来变成二进制的形式来进行存储。
num = int(input())
res = []
while num>=1:
    b =num%2
    num =num//2
    res.append(b)

print("".join(list(map(str,res))))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# 十进制的变成八进制。
while(True):
    try:
        a = int(input())
        o = 8
        p = 0
        r = []
        while a>=o:
            p = a % o
            a = a // o
            r.append(p)
        r.append(a)
        r = r[::-1]
        print("".join(list(map(str, r))))
    except:
        break










