

# 给定一个数字来判断是否为等差数列的结果值。



n = int(input())
nums = list(map(int,input().split(" ")))

res = True1
nums.sort()
cha = nums[1] - nums[0]

for i in range(2,n):
	if nums[i]-nums[i-1]!=cha:
		res = False 

if res:
	print("Possible")
else:
	print("Impossible")


