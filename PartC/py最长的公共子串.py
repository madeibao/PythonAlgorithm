

# 两个字符串的最长的公共的子串
'''
abcdefghijklmnop
abcsafjklmnopqrstuvw

'''

# 输出结果:
# jklmnop


# 保持的是 s1 的长度小于 s2的长度。


while True:
    try:
        s1 = input().strip()
        s2 = input().strip()
        if s1 == '' or s2 == '':
            break
        n = 0
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        for i in range(len(s1)):
            for j in range(i + 1, len(s1)):
                sub = s1[i:j+1]
                if sub in s2 and j - i > n:
                    n = j - i
                    sub1 = sub
        print(''.join(sub1))
    except:
        break


