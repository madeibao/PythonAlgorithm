
# 在一个螺旋的矩阵中，寻找个位数字为7，十位数字为奇数的内容。


def helper(n):
    a = n % 10
    b = (n // 10) % 10
    return a == 7 and b % 2


tmp = input().split()

try:
    M = int(tmp[0])
    N = int(tmp[1])
    assert 10 <= M <= 1000 and 10 <= N <= 1000
    up, right, down, left = 0, N-1, M-1, 0
    idx = 0
    res = []
    while up <= down and left <= right:
        for i in range(left, right+1, 1):
            idx += 1
            x = up
            y = i
            if helper(idx):
                res.append([x, y])

        up += 1

        for i in range(up, down+1, 1):
            idx += 1
            x = i
            y = right
            if helper(idx):
                res.append([x, y])

        right -= 1

        if left == right or up == down:
            break

        for i in range(right, left-1, -1):
            idx += 1
            x = down
            y = i
            if helper(idx):
                res.append([x, y])

        down -= 1

        for i in range(down, up-1,-1):
            idx += 1
            x = i
            y = left
            if helper(idx):
                res.append([x, y])

        left += 1
    res = str(res).replace(" ", "")
    print(res)
except:
    print("[]")

