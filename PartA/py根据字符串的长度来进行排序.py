
4
sky is grey
cold
very cold
3
it is good enough to be proud of
good
it is quite good


# 输出排序的结果值
#--------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
cold
very cold
sky is grey


good
it is quite good
it is good enough to be proud of


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    try:
        n = int(input())
        s = []
        for i in range(n):
            ss = input()
            if ss!='stop':
                s.append(ss)
            else:
                break
        s = sorted(s, key = lambda x: len(x))
        for i in s:
            print(i)
    except:
        break




