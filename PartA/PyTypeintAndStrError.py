# 像以下的情况就会极易出错

"""
i = 0
while i <= 100:
	sum += i   #这里的sum没有初始化的操作，就会被认为是一个字符串，字符串和数字怎么能取和呢。
	i += 1     
print(sum）

"""



i = 0
sum = 0   #这里的sum一定要初始化，要不然会当作字符串来进行处理。
while i <= 100:
# for i in range(0,101,1):
    sum += i
    i += 1   
print(sum)








