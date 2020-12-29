

# 求一个字符串的编码，最少需要多少位置就能够满足编码
# 哈夫曼的编码思想。

import sys
while True:
    try:
        s=sys.stdin.readline().strip()
        if s=='':
            break
        a=[]
        for i in set(s):
            a.append(s.count(i))

        a.sort()
        res=0
        while len(a)>1:
            t1,t2=a.pop(0),a.pop(0)
            res+=t1+t2
            a.append(t1+t2)
            a.sort()
        print(res)
    except:
        break

# 基本思想就是构建大顶堆的过程。


import sys

while True:
	try:
		s = sys.stdin.readline().strip()
		if s=="":
			break

		a = []

		for i in set(s):
			a.append(s.count(i))

		# 得到的是一组数字的值，代表的是每一个单词的出现的次数。
		a.sort()
		res = 0
		while len(a) > 1:
			t1 = a.pop(0)
			t2 = a.pop(0)
			res += t1+t2
			a.append(t1+t2)
			# 每次的结果只值都进行更行排序。
			a.sort()
		print(res)
	except:
		break

