#coding=utf-8
# ----————————--------------
【题目】

　　给定一个字符串 str, 求其中全部数字串所代表的数字之和。

【要求】

忽略小数点，例如 “A1.3”，其中包含两个数字 1 和 3.
如果紧贴数字子串的左侧出现字符"-"， 当连续出现的数量为奇数时，则数字视为负，连续出现的数量为偶数时，则数字视为正。比如，“A-1BC--12”， 其中包含数字 -1 和 12.
若字符串的长度为N，时间复杂度为 O(N)， 额外空间复杂度为 O(1)
【举例】

　　str="A1CD2E33", 返回 36。

　　str="A-1B--2C--D6E", 返回7。
# 两个负号的结果会蜕变成正好。
#------------------------------------------------------------------------------------------------
# A-1B--2C--D6E

import sys
if __name__ == "__main__":
    def sum_of_int(s):
        sums, num, pos = 0, 0, 1
        if s == None:
            return 0
        for i in range(len(s)):
            if 48 <= ord(s[i]) <= 57:
                num = num * 10 + int(s[i])*pos
            else:
                sums += num
                num = 0
                if s[i] == '-':
                    if i-1 > -1 and s[i-1] == '-':
                        pos = -pos
                    else:
                        pos = -1
                else:
                    pos = 1
        sums=sums+num
        return sums 
    e=sys.stdin.readline().strip()
    result=sum_of_int(e)
    print (result)





