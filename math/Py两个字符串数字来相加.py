


# 两个字符串的数字来进行相加求和。

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        from itertools import zip_longest
        res = ""
        carry = 0
        zero = ord('0')
        for a, b in zip_longest(num1[::-1], num2[::-1], fillvalue = "0"):
            carry, mod = divmod(ord(a) - zero + ord(b) - zero + carry, 10)
            res =  str(mod) + res
        if carry > 0:
            res = "1" + res
        return res


if __name__ == "__main__":
	s = Solution()
	str2 = "1223"
	str3 = "2323"

	print(s.addStrings(str2, str3))

	