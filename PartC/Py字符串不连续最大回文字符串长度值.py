

# 最大回文子串是被研究得比较多的一个经典问题。最近月神想到了一个变种，
# 对于一个字符串，如果不要求子串连续，那么一个字符串的最大回文子串的最大长度是多少呢。
# 因为在本题中，不要求回文子串连续，故最长回文子串为aba(或ada、aca)
# 因为不要求子串连续，所以字符串abc的子串有a、b、c、ab、ac、bc、abc7个


# adbca

# 返回的结果为3


s = input()
m = dict()
def getMax(s):
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    elif s[0] != s[-1]:
        if s in m:
            return m[s]
        else:
            tmp = max(getMax(s[1:]), getMax(s[:-1]))
            m[s] = tmp
            return tmp
    else:   # 首尾的两个字符相等。
        if s in m:
            return m[s]
        else:
            tmp = max(2 + getMax(s[1:-1]), getMax(s[1:]), getMax(s[:-1]))
            m[s] = tmp
            return tmp


print(getMax(s))


















