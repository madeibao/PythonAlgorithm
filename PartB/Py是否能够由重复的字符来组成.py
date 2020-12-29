
# 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

# 示例 1:

# 输入: "abab"
# 输出: True
# 解释: 可由子字符串 "ab" 重复两次构成。
# 1
# 2
# 3
# 示例 2:

# 输入: "aba"
# 输出: False
# 1
# 2
# 示例 3:

# 输入: "abcabcabcabc"
# 输出: True
# 解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
# ————————————————
# 版权声明：本文为CSDN博主「coordinate_blog」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_17550379/article/details/103994758



class Solution():
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (2 * s)[1:-1]

if __name__ == "__main__":
     s = Solution()
     print(s.repeatedSubstringPattern("abab"))


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        f = [0] * (n + 1)
        f[0], i, j = -1, 0, -1
        while i < n:
            while j != -1 and s[j] != s[i]:
                j = f[j] 
            i += 1
            j += 1
            f[i] = j
        return f[-1] and n % (n - f[-1]) == 0
