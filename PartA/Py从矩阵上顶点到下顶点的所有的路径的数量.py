




while True:
    try:
        def getnum(n, m):
            if n == 0 and m == 0:
                return 0
            if n == 0 or m == 0:
                return 1
            return getnum(n-1, m)+getnum(n, m-1)

        a, b = map(int, input().strip().split(" "))
        print(getnum(a, b))
    except:
        break


# 按照空格来进行分割的结果为
# 2 2
# 6