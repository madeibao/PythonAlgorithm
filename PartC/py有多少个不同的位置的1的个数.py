


# 两个数字的二进制的表示中， 不相同的个数来统计


a, b = map(int, input().split(" "))
temp = a^b 
res =0
while temp!=0:
    temp= temp&(temp-1)
    res+=1
print(res)

