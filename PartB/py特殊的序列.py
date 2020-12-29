
num = int(input())

def f(x):
	ten_sum = 0
	while x:
		ten_sum += x%10
		x =x //10

	return ten_sum

def g(x):
	bina  = bin(x)
	binaCount = bina.count('1')
	return binaCount

count = 0

for i in range(1, n+1):
	if f(i)==g(i):
		count += 1

print(count)

