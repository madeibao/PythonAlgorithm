

class Solution():
	def getWeekDay(self, day, month, year):
		from datetime import datetime
		temp = ["Friday", "Saturday", "Monday", "Tuesday", "Wednesday","Thursday"]

		day1 = datetime.strptime('1971-01-01','%Y-%m-%d')
		day2 = datetime.strptime(str(year)+'-'+str(month)+'-'+str(day),'%Y-%m-%d')

		return temp[(day2-day1).days%7]


if __name__ == '__main__':

	s = Solution()
	print(s.getWeekDay(26, 10, 2019))