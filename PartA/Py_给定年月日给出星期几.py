
# Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。
# Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
# 时间间隔是以秒为单位的浮点小数。
# 每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
# Python 的 time 模块下有很多函数可以转换常见日期格式。如函数time.time()用于获取当前时间戳, 如下实例:
# 1971年1月1日 是星期五


class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        d = 0  # 代表的是日期的总的天数内容。
        a = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   # 由于是从0开始计数的内容。
        for i in range(1971,year):
            if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
                d += 366
            else:
                d += 365
        for i in range(1,month):
            if i == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
                d += 29
            else:
                d += m[i-1]
        d += day    # 加上日期的内容。
        
        return a[d % 7 - 1]


if __name__ == "__main__":
	cc = Solution()
	print(cc.dayOfTheWeek(6, 9, 2018))

