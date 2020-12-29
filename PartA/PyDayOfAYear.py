



import datetime

m = int(input())
for i in range(m):
    temp = list(map(int, input().split()))
    date1 = datetime.date(temp[0], temp[1], temp[2])
    date2 = datetime.date(temp[0], 1, 1)
    sub = (date1-date2).days+1
    print(sub)






# 首先是测试数据
# 其次按照这种格式输入 1995 8 11


# 首先输入n个测试数据内容。
# 然后输入年分和日期。按照空格分割。




