
# 方法1----------------------------------------------------------------

def isPrime(num):
    for i in range(num):
        for j in range(2, num):
            if i % j == 0:
                break
        else:
            return True

# ----------------------------------------------------------------
# ---------------------------------------------------------------------------

# 方法2
from math import sqrt
def isPrime(num):
    for i in range(num):
        for j in range(2, int(sqrt(num))):
            if i % j == 0:
                break
        else:
            return True


# 方法3：

from math import sqrt
 
def isPrime(num):
    if num == 2 or num == 3:   # 两个较小的数进行处理
        return True
    if num % 6 != 1 and num % 6 != 5:  # 不在6的倍数的两侧的一定不是质数
        return False
    tmp = int(sqrt(num))
    for i in range(5, tmp+1):  # 在6的倍数两侧的也可能不是质数
        if num % i == 0 or num % (i+2) == 0:
            return False
    return True  # 剩下的全是质数



