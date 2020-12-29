

class Solution:
    def reformat(self, s: str) -> str:
    	alpha = []
    	nums = []

    	for i in s:
    		if i.isdigit():
    			nums.append(i)
    		else:
    			alpha.append(i)

    	res =""
    	if abs(len(alpha)-len(nums))<=1:
    		if len(nums)>=len(alpha):
    			for i in range(len(alpha)):
    				res = res+nums[i]+alpha[i]
    			if len(nums)>len(alpha):
    				res += nums[-1]

    		else:
    			for i in range(len(nums)):
    				res = res+alpha[i]+nums[i]

    			if len(alpha)>len(nums):
    				res += alpha[-1]
    	else:
    		return ""

    	return res


if __name__=="__main__":
	s= Solution()
	str2 = "a0b1c2"
	print(s.reformat(str2))




