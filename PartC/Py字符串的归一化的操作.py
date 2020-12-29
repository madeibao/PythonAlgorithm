
'''
通过键盘输入一串小写字母(a~z)组成的字符串。
请编写一个字符串归一化程序，统计字符串中相同字符出现的次数，并按字典序输出字符及其出现次数。
例如字符串"babcc"归一化后为"a1b2c2"


输入描述:
每个测试用例每行为一个字符串，以'\n'结尾，例如cccddecca
输出描述:
输出压缩后的字符串ac5d2e
示例1
输入
复制
dabcab
输出
复制
a2b2c1d1
'''

#================================================================
#=================================================================


import operator
def sort2(str2):
	list2 = list(str2)

	dict2 = {}

	for i in list2:
	    dict2[i] = dict2.get(i, 0) + 1

	# 根据字典的键来进行排序。
	test_data_4 = sorted(dict2.items(), key=operator.itemgetter(0))

	# 得到的结果是一个元组，然后求排序之后的结果值。
	list3 = []
	for key in test_data_4:
		list3.append(str(key[0]))
		list3.append(str(key[1]))

	return "".join(list3)


if __name__ == '__main__':
	str2 = input()
	print(sort2(str2))


# 方法2
# 超级简单

# 首先是变成集合的形式，来保证字符串的唯一。
string = input()
for i in sorted(list(set(string))):
    item = string.count(i)
    print(i + str(item), end = '')




