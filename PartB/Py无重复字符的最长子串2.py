



# 求一个字符串中的无重复字符的最长的子串。
# 没有重复字符的最长的子串，不是子序列，所以是连续的。


class Solution:
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        res = []
        for i in s:
            while i in res:
                res.pop(0)
            res.append(i)
            max_length = max(max_length, len(res))
        return max_length


if __name__ == "__main__":
    s = Solution()
    str2 = "abcdefghijklmnopqrstuvwxyzz"
    print(s.lengthOfLongestSubstring(str2))





