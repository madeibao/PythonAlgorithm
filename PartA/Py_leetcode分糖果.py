

class Solution():
	def candy(self,num):
		if num==None:
			return 0
		len1 = len(num)
		dp1 = [1 for i in range(len1)]
		dp2 = [1 for i in range(len1)]
		sum1 = 0
		for i in range(1,len1):
			if num[i]>num[i-1]:
				dp1[i] = dp1[i-1] + 1
			if i in range(len1-2,-1,-1):
				dp2[i] = dp2[i+1] + 1

		for i in range(len1):
			sum1 += max(dp1[i],dp2[i])

		return sum1


cc = Solution()
print(cc.candy([1, 0, 2]))













