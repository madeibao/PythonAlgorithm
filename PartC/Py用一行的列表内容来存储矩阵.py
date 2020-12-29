



矩阵为
现在把矩阵的元素内容变成一行的形式来进行存储。


nums = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]

num2 = []

for i in range(len(nums)):
	print(nums[i])
	num2 += nums[i]

print(num2)


另外的一种写法：


for i in range(len(nums)):
	num2.extend(nums[i])

print(num2)








