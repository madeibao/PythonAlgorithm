
def is_palindrom(s):
	if(len(s) < 2):
		return True   
	if(s[0] == s[-1]):     
	    return is_palindrom(s[1:-1])   # 注意字符串的截取操作，是包括开始，不包括结尾。
	else:      
	    return False  

name1 = 'ABBA'
name2 = '12344321'
print(is_palindrom(name1))
print(is_palindrom(name2))







# 切片操作（slice）可以从一个字符串中获取子字符串（字符串的一部分）。
# 我们使用一对方括号、起始偏移量start、终止偏移量end 以及可选的步长step 来定义一个分片。
# 格式： [start:end:step]
# • [:] 提取从开头（默认位置0）到结尾（默认位置-1）的整个字符串
# • [start:] 从start 提取到结尾
# • [:end] 从开头提取到end - 1
# • [start:end] 从start 提取到end - 1
# • [start:end:step] 从start 提取到end - 1，每step 个字符提取一个
# • 左侧第一个字符的位置/偏移量为0，右侧最后一个字符的位置/偏移量为-1