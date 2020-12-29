# 题目描述
# 用一维数组存储学号和成绩，然后，按成绩排序输出。
# 输入描述:
# 输入第一行包括一个整数N(1<=N<=100)，代表学生的个数。
# 接下来的N行每行包括两个整数p和q，分别代表每个学生的学号和成绩。
# 输出描述:
# 按照学生的成绩从小到大进行排序，并将排序后的学生信息打印出来。
# 如果学生的成绩相同，则按照学号的大小进行从小到大排序。
# 示例1
# 输入
# 复制
# 3
# 1 90
# 2 87
# 3 92
# 输出
# 复制
# 2 87
# 1 90
# 3 92

#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------


N= int(input())
data = []
for i in range(N):
    data.append(input().split())
# data = sorted(data, key = lambda x:int(x[0]))
output = sorted(data, key = lambda x:(x[1],x[0]))

for i in range(N):
    print(output[i][0], output[i][1])