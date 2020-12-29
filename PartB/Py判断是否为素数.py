
num = int(input())

def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
print(isPrime(num))

#------------------------------------------------------------------------------------------------
import timeit
from math import sqrt

def isPrimes1(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def isPrimes2(n):   # 使用第二种方法能够显著的降低时间的消耗。
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


print(timeit.timeit("isPrimes1(100)", setup="from chapter01 import isPrimes1", number=10000))
print(timeit.timeit("isPrimes2(100)", setup="from chapter01 import isPrimes2", number=10000))
