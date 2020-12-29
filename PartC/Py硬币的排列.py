
#
# #
# # #
# # # #
# # # # #
# # # # # #

# 1 3 6 10 15 21

#
# #
# #


你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

给定一个数字 n，找出可形成完整阶梯行的总行数。

n 是一个非负整数，并且在32位有符号整型的范围内。

示例 1:

n = 5

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤

因为第三行不完整，所以返回2.


示例 2:

n = 8

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤



from math import floor, sqrt


class Solution:
    def arrangeCoins(self, n: int) -> int:
        list2 = []
        
        for i in range(n):
            if (i+1)*i//2 <= n:
                list2.append((i+1)*i//2)

        temp = 0
        for j in range(len(list2)):
            if n == list2[j]:
                temp = j
            elif n > list2[j]:
                temp = j
        return temp


# 运用数学公式，二次函数，开口向下的二次函数内容，来求解。
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return floor(sqrt(1/4+2*n)-1/2)


if __name__ == '__main__':
    s = Solution()
    print(s.arrangeCoins(18042893))
