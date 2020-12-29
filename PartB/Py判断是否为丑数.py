
# 编写一个程序，找出第 n 个丑数。
# 丑数就是只包含质因数 2, 3, 5 的正整数。


# 下面的算法用来判断一个数字是否为丑数。
def isugly(num):
    temp = 2
    bool2 = True
    while num > temp:
        k = num % temp
        if k == 0:
            num = num/temp
        else:
            temp += 1
        if temp > 5:
            bool2 = False
            break
    return bool2


# 下面的是算法二的实现内容。
# 判断是否为丑数的内容

def isuglynum(num):
    while num % 2 == 0:
        num /= 2
    while num % 3 == 0:
        num /= 3
    while num % 5 == 0:
        num /= 6
    return num == 1


print(isuglynum(14))


# 下面的算法判断第n个丑数。


class Solution():
    def getugly(self, nums):
        if nums < 7: return nums
        p1, p2, p3 = 0, 0, 0
        arr = [1]
        while len(arr) < nums:
            temp = min(arr[p1]*2, min(arr[p2]*3, arr[p3]*5))
            arr.append(temp)

            if temp == arr[p1]*2:
                p1 += 1
            if temp == arr[p2]*3:
                p2 += 1
            if temp == arr[p3]*5:
                p3 += 1
        return arr[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.getugly(10))












