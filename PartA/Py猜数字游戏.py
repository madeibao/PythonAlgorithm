# 你正在和你的朋友玩 猜数字（Bulls and Cows）游戏：你写下一个数字让你的朋友猜。每次他猜测后，
#你给他一个提示，告诉他有多少位数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位数字猜对了但是位置不对（称为“Cows”, 奶牛）。你的朋友将会根据提示继续猜，直到猜出秘密数字。

# 请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。

# 请注意秘密数字和朋友的猜测数都可能含有重复数字。

# 示例 1:

# 输入: secret = "1807", guess = "7810"

# 输出: "1A3B"

# 解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。

# 示例 2:

# 输入: secret = "1123", guess = "0111"

# 输出: "1A1B"

# 解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛。

import collections
def getHint(secret, guess):
    """
        1. 先计算相等的字符a的个数.
        2. 把不相等的字符进行数量的统计, 然后计算b的个数
    """
    a, b, s1, s2 = 0, 0, [], []
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            a += 1
        else:
            s1.append(secret[i])
            s2.append(guess[i])
    counter1,counter2 = collections.Counter(s1), collections.Counter(s2)
    for k in counter1.keys():
        if k in counter2:
            b += min(counter1[k], counter2[k])
    
    return f'{a}A{b}B'


class Solution:
    def getHint(self, secret, guess):
        A,B=0,0
        dic1,dic2={},{}
        siz=len(secret)
        for i in range(siz):
            if secret[i]==guess[i]:
                A+=1
            else:
                if secret[i] not in dic1:
                    dic1[secret[i]]=1
                else:
                    dic1[secret[i]]+=1
                if guess[i] not in dic2:
                    dic2[guess[i]]=1
                else:
                    dic2[guess[i]]+=1
        for x in dic1:
            if x in dic2:
                B+=min(dic1[x],dic2[x])
        return str(A)+'A'+str(B)+'B'




print(getHint("1807", "7810"))
print(getHint("1123", "0111"))
