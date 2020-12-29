


# 保留字符串中的第一次出现的字符，每个字符都保持不同。
string_set, str1 = set(), ""			# 创建一个空集合，一个空字符串。
for char in input():
    if char not in string_set:
        string_set.add(char)
        str1 += char

print(str1)


# 创建一个空的集合，必须是set(), {}用来创建一个空的字典的操作。


"""
例如：
asdfasdfの2322323523
asdfの235
8

"""









