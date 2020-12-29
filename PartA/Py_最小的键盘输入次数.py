
cases =['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']


def hit(s, i=0):
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1+(s[0] not in cases[i] and 1 or 0)
    else:
        if s[0] in cases[i]:
            return 1+hit(s[1:], i)
        else:
            return 2+hit(s[1:], 1-i)


print(hit("AaAAAA"))

# 默认状态是小写字母。


