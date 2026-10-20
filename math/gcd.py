

import math

def gcd(a:int, b:int) -> int:
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def lcm(a:int, b:int) -> int:
    return abs(a * b) // gcd(a, b)


print(lcm(12, 15))
print(gcd(12, 24))


print(math.gcd(12, 24))
print(math.lcm(12, 24))

