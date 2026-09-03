


# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 ...
# 现在求第 n 项目是多少。

i = 1
count = 0
num = int(input())
while True:
    for j in range(0, i):
        count += 1
        if count == num:
            break
    if count == num:
        break
    else:
        i = i + 1


print(i)



