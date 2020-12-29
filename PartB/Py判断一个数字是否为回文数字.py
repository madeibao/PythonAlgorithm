


# 判断一个数字内容，然后确定，数字内容是否为回文的数字
# 例如121 是回文数字
# 131是回文数字



class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1] 


if __name__ == "__main__":
    s  = Solution()
    print(s.isPalindrome(121))