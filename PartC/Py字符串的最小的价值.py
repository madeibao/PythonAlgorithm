


有一种有趣的字符串价值计算方式:统计字符串中每种字符出现的次数,然后求所有字符次数的平方和作为字符串的价值
例如: 字符串"abacaba",里面包括4个'a',2个'b',1个'c',于是这个字符串的价值为4 * 4 + 2 * 2 + 1 * 1 = 21
牛牛有一个字符串s,并且允许你从s中移除最多k个字符,你的目标是让得到的字符串的价值最小。
输入描述:
输入包括两行,第一行一个字符串s,字符串s的长度length(1 ≤ length ≤ 50),其中只包含小写字母('a'-'z')。
第二行包含一个整数k(0 ≤ k ≤ length),即允许移除的字符个数。
输出描述:
输出一个整数,表示得到的最小价值
示例1
输入
复制
aba
1
输出
复制
2

#-----------------------------------------------------------------------------------------
#_----------------------------------------------------------------------------------------


from collections import Counter
import operator

str2 = input()
num = int(input())

dict2 = Counter(str2)
test_data_4 = sorted(dict2.items(), key=operator.itemgetter(1), reverse=True)

res= []

for i in test_data_4:
	res.append(i[1])

for i in range(num):
	res[0] -=1
	res.sort(reverse=True)


print(sum(map(lambda c: c ** 2, res)))


