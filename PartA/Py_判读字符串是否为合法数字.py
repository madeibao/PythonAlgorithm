

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try:
            p = float(s)
            return True
        except:
            return False


ss = Solution()
print(ss.isNumeric("12e+4.3"))  # 不合法。


"-1E-16"  # 这种为合法的数字。











