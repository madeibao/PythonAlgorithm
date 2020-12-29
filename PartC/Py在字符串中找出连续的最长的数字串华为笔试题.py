# 输入描述:
# 输入一个字符串。
# 输出描述:
# 输出字符串中最长的数字字符串和它的长度。如果有相同长度的串，则要一块儿输出，但是长度还是一串的长度

# 输入：
# abcd12345ed125ss123058789
# 输出：
# 123058789,9

# 输入：
# 8749r6k4nugdm04p5b1yhegi8hiq3937
# 输出：
# 87493937,4



while True:
    try:
        class Solution:
            def lengthOfLongestSubstring(self, str2):
                s = list(str2)
                cnt = 0
                res = 0
                list2 = []
                str3 = str()
                for num in s:
                    if num >= '0' and num <= '9':
                        str3 += num
                        cnt += 1
                        res = max(res, cnt)
                        list2.append(str3)
                    else:
                        cnt = 0
                        str3 = ""   # 重新的清空字符串的内容。

                str4 = str()
                for i in list2:
                    if len(i) == res:
                        str4 += i

                return str4 + "," + str(res)

        if __name__ == '__main__':
            s = Solution()
            s2 = input()
            print(s.lengthOfLongestSubstring(s2))

    except:
        break
#================================================================
#==========-----------------------------------------------------------------------------

while True:
    try:
        a = input()
        maxLen, maxStrs, curLen, curStr = 0, [], 0, ""
        for i, v in enumerate(a):
            if v.isnumeric():
                curLen += 1
                curStr += v
                if curLen > maxLen:
                    maxLen = curLen
                    maxStrs = [curStr]
                elif curLen == maxLen:
                    maxStrs.append(curStr)
            else:
                curLen = 0
                curStr = ""
        print("".join(maxStrs) + "," + str(maxLen))
    except:
        break



