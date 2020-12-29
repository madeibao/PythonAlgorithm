

# 给定一个数字判断是否为素数的数字。


import math

def is_prime(a):
    if a == 2 or a == 3 or a == 5 or a == 7:
        return True
    if a % 2 == 0:
        return False
    if (a+1) % 6 != 0 and (a-1) % 6 != 0:
        return False
    up = int(math.sqrt(a)) + 1
    for i in range(3, up, 2):
        if a % i == 0:
            return False
    return True


if __name__ == "__main__":
	print(is_prime(17))

