



# 字符串的左移动旋转。



class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        return s[n:]+s[:n]


ss = Solution()
str = input()
print(ss.LeftRotateString(str,3))


abcdefghijklmn
defghijklmnabc