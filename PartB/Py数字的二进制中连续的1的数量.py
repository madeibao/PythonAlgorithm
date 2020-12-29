

# 一个数字的二进制的表示中的，连续的一的数量。

while True:
    try:
        def lengthOfLongestSubstring(s):
            cnt = 0
            res = 0
            for num in s:
                if num == 1:
                    cnt += 1
                    res = max(res, cnt)
                else:
                    cnt = 0
            return res
        num = int(input())
        cc = bin(num)[2:]
        test = list(cc)
        test2 = [int(i) for i in test]

        print(lengthOfLongestSubstring(test2))
    except:
        break





