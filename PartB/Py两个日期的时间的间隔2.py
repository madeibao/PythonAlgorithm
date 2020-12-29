

class Solution():
    def daysBetweenDates(self, date1: str, date2: str) -> int:

    	def isReap(year):
    		if year%400 == 0:
    			return True
    		elif year%4==0 and year%100 != 0:
    			return True 
    		else:
    			return False

    	def getSub(year, month, day):

    		res = 0
    		month1 = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    		for i in range(1971, year):
    			if isReap(i):
    				res += 366
    			else:
    				res += 365

    		for i in range(1, month):
    			if i==2 and isReap(year):
    				res += 29
    			elif not isReap(year) and i==2:
    				res += 28
    			else:
    				res += month1[i]

    		return res+day

    	year1, month1,day1 = map(int, date1.split("-"))
    	year2, month2,day2 = map(int, date2.split("-"))

    	sub1 = getSub(year1, month1, day1)
    	sub2 = getSub(year2, month2, day2)
    	return abs(sub1 - sub2)


if __name__ == "__main__":
	s1 = "1995-08-11"
	s2 = "2020-04-30"

	s= Solution()
	day = s.daysBetweenDates(s1,s2)

	print(day)



