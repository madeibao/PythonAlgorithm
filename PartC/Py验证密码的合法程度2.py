题目描述
密码要求:

 

 

 

1.长度超过8位

 

 

 

2.包括大小写字母.数字.其它符号,以上四种至少三种

 

 

 

3.不能有相同长度超2的子串重复

 

 

 

说明:长度超过2的子串


输入描述:
一组或多组长度超过2的子符串。每组占一行

输出描述:
如果符合要求输出：OK，否则输出NG

示例1
输入
复制
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000
输出
复制
OK
NG
NG
OK

# ==================================
#----------------------------------------------------------------


import sys

def isLegal(str2):
	if len(str2)>8:
		return True
	else:
		return False 

def isLegal2(str3):
	for i in range(len(str3)-3):
		if str3[i:i+3] in str3[i+1:]:
			return False
			break
	return True

def isLegal3(str4):

	num = 0
	alA = 0
	ala = 0
	oth = 0

	list2 = list(str4)
	for i in list2:
		if '0'<= i<='9':
			num =1
		elif 'A'<= i<='Z':
			alA =1
		elif 'a'<= i<='z':
			ala =1  
		else:
			oth =1

	if num + alA + ala + oth >=3:
		return True
	else:
		return False 

while True:
	try:
		# str2 = sys.stdin.readline().strip('\n')
		str2 = input()
		if isLegal(str2) and isLegal2(str2) and isLegal3(str2):
			print("OK")
		else:
			print("NG")
	except:
		break
	



			








