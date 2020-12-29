



输入的字符只包含 L R


n = int(input())
str2  = input()
count = 0

# 首先模拟逆时针旋转
numbers =['N','W','S','E']

for i in range(len(str2)):
	if str2[i]=='L':
		count += 1
	else:
		count -= 1 

print(numbers[count%4])