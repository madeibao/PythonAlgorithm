
#2018年09月06日，我来到了南京邮电大学。

import time
import datetime


# 计算两个日期相差天数，自定义函数名，和两个日期的变量名。
def Caltime(date2):
    # %Y-%m-%d为日期格式，其中的-可以用其他代替或者不写，但是要统一，同理后面的时分秒也一样；可以只计算日期，不计算时间。
    date1 = time.strptime("2018-09-06", "%Y-%m-%d")
    date2 = time.strptime(date2, "%Y-%m-%d")
    # 根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    # 返回两个变量相差的值，就是相差天数
    return date2 - date1


# 判断日期是否为合法输入，年月日的格式需要与上面对应，正确返回True，错误返回False，注意大小写。
def is_date(str):
    try:
        time.strptime(str, "%Y-%m-%d")
        return True
    except:
        return False


if __name__ == '__main__':
    # 提示信息请根据实际情况更改
    while True:
        dt2 = input()
        if is_date(dt2) == True:
            break
        else:
            print('请输入正确的日期！！！请重新输入！！！')

    print(Caltime(dt2))
