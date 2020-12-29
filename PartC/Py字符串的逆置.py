def reverse1():
    s = input("please input a string: ")
    return s[::-1]


reverse1()
please input a string: yangyue!
'!euygnay'


2.使用递归
def reverse2(s):
	if s == "":
		return s
	else:
		return reverse2(s[1:]) + s[0]


s = 'yangxinyue'
reverse2(s)
'euynixgnay'
 

3.使用列表的reverse
def reverse3(s):
	l = list(s)
	l.reverse()
	print("".join(l))

reverse3('yangxinyue')
euynixgnay
 


