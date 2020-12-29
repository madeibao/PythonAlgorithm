


# 美团笔试题目：第一题的结果：
# 题目的意思是在一个数字的范围内，一个数相乘4倍后与自身是逆序的数字，就是字符串意义上的逆序。



def f1(n):
    r = []
    c = n // 4
    for i in range(1, c + 1):
        if str(4*i) == str(i)[::-1]:
            r.append(i)
    return r

while True:
    try:
        n = int(input())
        r = f(n)
        print(len(r))
        for i in r:
            print(str(i), ' ', str(i)[::-1])
    except:
        break


# ====================================================================
# ----------------------------------------------------------------------------------------------
# 把数字和逆序数字都添加进去。

N = int(input())
res = []
for i in range(1,N//4+1):
    ni = i*4
    if str(i)[::-1]==str(ni) and ni<=N:
        res.append([i,ni])
print(len(res))
for i in res:
    print(i[0],i[1]) 