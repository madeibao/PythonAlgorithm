

n = int(input())
res = 0
while n > 1:
    flag = 1
    t = int(n**0.5)
    for i in range(2,t+1):
        if n % i == 0:
            n /= i
            res += 1
            flag = 0
            break
    if flag:
        res += 1
        break
print(res)


