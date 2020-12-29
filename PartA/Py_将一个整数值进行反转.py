
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

# 示例 1:
# 输入: 123
# 输出: 321



#  示例 2:
# 输入: -123
# 输出: -321

# 示例 3:
# 输入: 120
# 输出: 21




class Solution(object):
    def reverse(self, x):
        maxi = 2147483647
        mini = -2147483648
        res = 0
        judge = True
        if x < 0:
            x = -x
            judge = False
            
        while x != 0:
            res = res * 10 + x % 10
            x = int(x / 10)

        if judge == False:
            res = -res
            
        if res > maxi or res < mini:
            return 0
        else:
            return res


cc = Solution()
print(cc.reverse(-321))







