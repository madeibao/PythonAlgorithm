
class Solution():
    def dayOfYear(self, date) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        date2 = date.split("-")
        year, month, day = int(date2[0]), int(date2[1]), int(date2[2])   # 首先要转化成整形的形式来进行存储。
        
        if(year%4==0 and year%100!=0) or year%400==0:
            days[1] +=1
        return sum(days[:month-1])+day


cc = Solution()
print(cc.dayOfYear("1995-8-11"))

#----------------------------------------------------------------
#----------------------------------------------------------------

def isreap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def dayOfYear(year, month, day) -> int:
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isreap(year):
        days[1] += 1
    return sum(days[:month - 1]) + day


while True:
    try:
        a, b, c = map(int, input().split())  # 这条语句就能够表示输入的句法。
        num = dayOfYear(a, b, c)

        if isreap(a) and num > 366:
            print(-1)
        elif not isreap(a) and num > 365:
            print(-1)
        else:
            print(num)
    except:
        break



# ------------------------------    
#------------------------------
# 一年之中的第几天的内容


y,m,d = map(int, input().rstrip().split(' '))
arr = [31,28,31,30,31,30,31,31,30,31,30,31]
res = sum(arr[:m-1]) + d
if y%400==0 or (y%100 and y%4==0):
    res += 1
print(res)


# 一年中的第几天的内容。

import sys
 
try:
    while True:
        line = sys.stdin.readline().strip()
        if line is None or line == "":
            break
        tmp = list(map(int, line.split(' ')))
        y, m, d = tmp[0], tmp[1]-1, tmp[2]
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            months[1] = 29
         
        if m == 0:
            print(d)
        else:
            print(sum(months[:m]) + d)
except:
    pass
         
         








