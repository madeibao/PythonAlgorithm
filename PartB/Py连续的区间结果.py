

n = int(input())

nums = list(map(int,input().split(" ")))

nums.sort()
res = 1

for i in range(1,len(nums)):
	if nums[i]!= nums[i-1]+1:
		res += 1

print(res)