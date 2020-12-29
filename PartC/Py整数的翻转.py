# 整数的翻转结果值。
# 123  = 321
# -123 = -321


while True:
    try:
        a = list(input())
        if a[0] == '-':
            aa = a[1:]
            aa.reverse()
            ret = ''.join(['-'] + aa)
        else:
            a.reverse()
            ret = ''.join(a)
        print(int(ret))
    except:
        break
