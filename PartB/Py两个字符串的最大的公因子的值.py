

# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2019/10/31 18:31
# @File: Test.py


class Solution(object):
    def gcd(self, m, n):
        if n > m:
            m, n = n, m
        if m % n == 0:
            return n
        return self.gcd(n, m % n)

    def gcdOfStrings(self, str1, str2):
        res = ""
        if str1 + str2 == str2 + str1:
            return str1[:self.gcd(len(str1), len(str2))]
        return res


if __name__ == "__main__":
    s2 ="ABABAB"
    s3 ="AB"
    s =Solution()
    print(s.gcdOfStrings(s2, s3))






