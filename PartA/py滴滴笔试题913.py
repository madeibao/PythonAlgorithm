

n = int(input())
str2 = input()
res = []
while len(str2) > 0:
    res.append(str2[:n])
    str2 = str2[n:]
res2 = []
for i in res:
    res2.append(i[::-1])
print("".join(res2))
