



给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.


class Solution:
    def lengthOfLongestSubstring(self, s):
        cnt = 0
        res = 0
        for num in s:
            if num == 1:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 0
        return res


cc = Solution()
print(cc.lengthOfLongestSubstring([1, 1, 0, 1, 1, 1]))

