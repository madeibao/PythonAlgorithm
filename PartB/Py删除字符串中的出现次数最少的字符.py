

abcdd
返回
dd

# 删除字符中的出现次数最少的字符的结果值
from collections import defaultdict


str2 = input()
dd = defaultdict(int)

for i in str2:
	dd[i] += 1

for i in dd:
	if dd[i] == min(dd.values()):
		str2 = str2.replace(i,"")
	print(str2)
