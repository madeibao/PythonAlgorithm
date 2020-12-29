import datetime


def function(year, month, day):
    date = datetime.date(year, month, day)
    return date.strftime('%j')           #%j十进制表示的每年的第几天


temp = list(map(int, input().split()))
print(function(temp[0], temp[1], temp[2]))         # 366

# 按照这种格式输入 1995 8 11

