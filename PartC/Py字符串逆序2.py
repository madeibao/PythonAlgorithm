
def nixv(s):
    sum = str()                        # 定义空字符串
    for i in reversed(range(len(s))):  # i逆序遍历
        sum = sum + s[i]               # 使单独的字符串组合成整体
    return sum                         # 返回字符串

s = input("请输入一个字符串:")
print(nixv(s))


# 方法二
s='wqrwqr123'
print(s[::-1])# 切片



# 方法三
from functools import reduce
s = '123456'
result = reduce(lambda x,y:y+x,s)
print(result)

# 这段代码的含义是反复的调用
'2'+'1'
'3'+'2'+'1'
'4'+'3'+'2'+'1'
'5'+'4'+'3'+'2'+'1'
'6'+'5'+'4'+'3'+'2'+'1'


# 所以最终的结果为逆序的形式。



# 方法四
def fan(str1):
    len1=len(str1)
    for i in range(len1):
        print(str1[len1-1-i],end='')
fan('asdfg')

