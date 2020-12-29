


# 最小公倍数 = 两数之积除以最大公约数


def lcm(x, y):
    #  获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm

print(lcm(3, 4))





# 最小公倍数 = 两数之积除以最大公约数
#----------------------------------------------------------------

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)
while True:
    try:
        a,b=map(int,input().split())
        print(lcm(a,b))
    except:
        break


