

# 两个数字的二进制的表示中，
# 共有多少个bit位置是不相同的。

a, b = map(int, input().split(" "))

temp = a^b
res = 0

while temp!=0:
	temp = temp&(temp-1)
	res+=1

print(res)

