

def fun2(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b


# 方法二
def getMaxcommpisor(a, b):
    if a < b:
        a, b = b, a     # 保证a大于b
    while a%b != 0:
        a, b = b, a%b
    return b

# 方法三

def gcd(p, q):
    if q == 0:
        return p
    return gcd(p, p % q)

# 方法4:
def func3(x, y):
    hcf = 0
    if x < y:
        smaller = x
    else:
        smaller = y

    for i in range(1, smaller+1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf



print(fun2(12, 24))

# 最小公倍数。


