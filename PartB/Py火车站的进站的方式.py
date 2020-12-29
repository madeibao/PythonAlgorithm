
# 题目描述
# 给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，每辆火车以数字1-9编号。要求以字典序排序输出火车出站的序列号。
# 输入描述:
# 有多组测试用例，每一组第一行输入一个正整数N（0<N<10），第二行包括N个正整数，范围为1到9。

# 输出描述:
# 输出以字典序从小到大排序的火车出站序列号，每个编号以空格隔开，每个输出序列换行，具体见sample。

# 示例1
# 输入
# 复制
# 3
# 1 2 3
# 输出
# 复制
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 2 1


#----------------------------------------------------------------
#----------------------------------------------------------------

from typing import List
def handle(waits, ins, outs, result: List):
	if not waits and not ins:
		result.append(outs)
	if ins:
		temp_outs = outs + ins[-1] + ' '
		handle(waits, ins[:-1], temp_outs, result)
	if waits:
		temp_ins = ins.copy()
		temp_ins.append(waits[0])
		handle(waits[1:], temp_ins, outs, result)  
   
n = int(input())
waits = input().strip().split(' ')
result = []
ins = []
outs = ''
handle(waits, ins, outs, result)
result = sorted(result)
for s in result:
    print(s)



