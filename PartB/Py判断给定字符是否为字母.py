


list2 = ['a','b','c']

def isalpha2(c):
	if ord(c)>=65 and ord(c)<=90 or ord(c)>=97 and ord(c)<=122:
		return True
	else:
		return False


for i in range(len(list2)):
	if isalpha2(list2[i]):
		print("True")
	else:	
		print("False")






判断是否为字母字符时，可以通过使用  ord()  方法。
def isalpha2(c):
	if ord(c)>=65 and ord(c)<=90 or ord(c)>=97 and ord(c)<=122:
		return True
	else:
		return False




