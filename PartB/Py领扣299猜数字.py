

你正在和你的朋友玩 猜数字（Bulls and Cows）游戏：你写下一个数字让你的朋友猜。
每次他猜测后，你给他一个提示，告诉他有多少位数字和确切位置都猜对了（称为“Bulls”, 公牛），
有多少位数字猜对了但是位置不对（称为“Cows”, 奶牛）。你的朋友将会根据提示继续猜，直到猜出秘密数字。

请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。

请注意秘密数字和朋友的猜测数都可能含有重复数字。

示例 1:

输入: secret = "1807", guess = "7810"

输出: "1A3B"

解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。

示例 2:

输入: secret = "1123", guess = "0111"

输出: "1A1B"

解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛。

ps: 默认的是两个字符串的内容是相等的。

#-----------------------------------------------------------------------------------------

import collections

class Solution():
    def getnum(self,secret, guess):
        size = len(secret)
        Anum = 0 
        Bnum = 0
        s1 = []
        s2 = []
        for i in range(size):
            if secret[i] == guess[i]:
                Anum += 1
            else:
                s1.append(secret[i])
                s2.append(guess[i])

        counter1 = collections.Counter(s1)   # 计数器的内容。
        counter2 = collections.Counter(s2)   # 第二个部分的内容进行计数。
        for i in counter1.keys():
            if i in counter2:
                Bnum += min(counter2[i], counter1[i])

    retunr str(Anum)+"A"+str(Bnum)+"B"

if __name__ == "__main__":
    s = Solution()
    print(s.getnum("1123","0111"))




