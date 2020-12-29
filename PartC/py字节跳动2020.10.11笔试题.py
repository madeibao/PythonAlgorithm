

'''

5 3
1 1
2 2
3 3
4 4
4 4
'''

a, b = map(int, input().split(" "))

dict2 = {}
for i in range(a):
    x, y = map(int, input().split(" "))
    if x not in dict2.keys():
        dict2[x] = y
    else:
        dict2[x] += y

res = []
l = sorted(dict2.items(), key=lambda s:(-s[1], -s[0]))
for i in l[:b]:
    res.append(i[0])

print(res)




