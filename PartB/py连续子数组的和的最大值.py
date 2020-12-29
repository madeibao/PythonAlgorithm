

num = int(input())
list2 = list(map(int, input().split(" ")))

sum2 = list2[0]
max2 = list2[0]

for i in range(1, num):
	sum2 = sum2+list2[i] if sum2>0  else list2[i]
	if sum2>max2:
		max2 = sum2

print(max2)


# -------------------------------------------------------------------


3
-1 2 1
3