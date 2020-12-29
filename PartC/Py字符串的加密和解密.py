


题目描述
1、对输入的字符串进行加解密，并输出。

2加密方法为：

当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；

当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；

其他字符不做变化。

3、解密方法为加密的逆过程。

 

接口描述：

    实现接口，每个接口实现1个基本操作：

void Encrypt (char aucPassword[], char aucResult[])：在该函数中实现字符串加密并输出

说明：

1、字符串以\0结尾。

2、字符串最长100个字符。

 

int unEncrypt (char result[], char password[])：在该函数中实现字符串解密并输出

说明：

1、字符串以\0结尾。

    2、字符串最长100个字符。


输入描述:
输入说明
输入一串要加密的密码
输入一串加过密的密码

输出描述:
输出说明
输出加密后的字符
输出解密后的字符

示例1
输入
复制
abcdefg
BCDEFGH
输出
复制
BCDEFGH
abcdefg



#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------


while True:
	try:
		str1 = input()
		str2 = input()

		a = []

		for i in str1:
			if i.isdigit():
				if i == '9':
					a.append('0')
				else:
					a.append(str(int(i)+1))
			elif i.islower():
				if i=='z':
					a.append('A')
				else:
					a.append(chr(ord(i)-31))
			elif i.isupper():
				if i=='Z':
					a.append('a')
				else:
					a.append(chr(ord(i)+33))
			else:
				a.append(i)
		print("".join(a))

		l = []

		for j in str2:
			if j.isdigit():
				if j=='0':
					l.append('9')
				else:
					l.append(str(int(j)-1))
			elif i.isupper():
				if j=='A':
					l.append('z')
				elif:
					l.append(chr(ord(j)+31))
			elif j.islower():
				if j == 'a':
					l.append('Z')
				else:
					l.append(chr(ord(j)-33))
			else:
				l.append(s)

		print("".join(l))

	except:
		break

