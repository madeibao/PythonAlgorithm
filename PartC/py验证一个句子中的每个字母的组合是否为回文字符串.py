


# 判断一个字符串中的字符，去掉标点符号等符号之后
# 只包含有字母和数字，判断是否为回文字符串。


class Solution:
    def isPalindrome(self, s: str) -> bool:
        def fun2(s):
            return s.isalnum()

        def fun3(s):
            return "".join(s).lower()

        res = list(filter(fun2, s))
        temp = fun3(res)
        return temp[::-1] == temp


if __name__ == "__main__":
    s = Solution()
    str2 = "A man, a plan, a canal: Panama"
    print(s.isPalindrome(str2))

