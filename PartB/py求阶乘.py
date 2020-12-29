



import math
num = int(input())
value = math.factorial(num)
str2 = str(value).rstrip("0")[-1]
print(str2)