


# 给出一个数字，判断是不是水仙花数字。



def hui(x):
	num=int(x)   	 # 字符串转换成整形。
	n=list(str(x))   # 将之转变成一系列的字符['1','2','3','4']
	s=0
	for i in n:
		s+=int(i)**3
	if s==num:
		return True
	return False

x =int(input())
print(hui(x))





