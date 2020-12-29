


# 题目描述
# 假设你正在玩跳格子（所有格子排成一个纵列）游戏。需要 跳完n 个格子你才能抵达终点。
# 每次你可以跳 1 或 2 个格子。你有多少种不同的方法可以到达终点呢？
# 注意：给定 n 是一个正整数。
# 输入描述:
# 格子数n
# 输出描述:
# 跳完n个格子到达终点的方法
# 示例1
# 输入
# 复制
# 2
# 输出
# 复制
# 2


# 递归版本的内容，时间复杂度过于大。 所以不宜采用。
def getnum(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return getnum(n-1)+getnum(n-2)


n = int(input().strip())
print(getnum(n))



# 非递归版本，时间复杂度不是特别大。

def jump(n):
    result = [0, 1]
    if n < 2:
        return result[n]
    a, b = 1, 1
    for i in range(2, n + 1):
        sum = a + b
        a = b
        b = sum
    return sum


if __name__ == '__main__':
    n = int(input())
    print(jump(n))



# 方法3




def jump(n):
    result = [0, 1]
    if n < 2:
        return result[n]
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = b, a+b
    return b

if __name__ == '__main__':
    n = int(input())
    print(jump(n))



