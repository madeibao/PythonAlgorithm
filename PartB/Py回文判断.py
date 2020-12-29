
+

s= input("请输入一个字符串")
if not s:
	print("字符串不能为空")
	s=input("请输入一个字符串")

l = reversed(list(s))
if list(s)==list(l):
	print("是回文。")
else:
	print("不是回文。")



	