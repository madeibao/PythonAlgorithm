

n = int(input())

res = 0
while n:
    n &= (n - 1)
    res += 1

print(res)



