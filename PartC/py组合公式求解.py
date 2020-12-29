

C(n,m) = C(n, n-m)
C(5,2) = C(5,3)
C(n, m) = n!//(m!*(n-m)!)

#------------------------------------------------------------------
#------------------------------------------------------------------


def helper(n):
    if n == 1:
        return n
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def getValue(n, m):
    first = helper(n)
    second = helper(m)
    third = helper(n - m)
    return first // (second * third)


if __name__ == "__main__":
    print(getValue(5, 3))
    print(getValue(5, 2))

