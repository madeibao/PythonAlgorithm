

例如10

有 3+7 和 5+5 
一共两个数对，所以是返回结果为2



from math import sqrt

n = int(input())
res = []


def isPrimes2(n):
    if n > 1:
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for x in range(3, int(sqrt(n) + 1), 2):
            if n % x == 0:
                return False
        return True
    return False

# 算法的精髓的部分值。
for i in range(1, n//2+1):
    if isPrimes2(i) and isPrimes2(n-i):
        res.append((i, n-i))

res2 = []
for i in res:
    res2.append(list(sorted(i)))

print(len(res2))


