

s = input()
result = ""

for i in range(len(s)):
	if i==0:
		result += s[i].upper()
	elif s[i-1]==' ':
		result += s[i].upper()
	else:
		result += s[i]

print(result)



# 输入一个字符串，代表的是整个句子的内容，然后将每一个单词的首字母都进行大写。。
