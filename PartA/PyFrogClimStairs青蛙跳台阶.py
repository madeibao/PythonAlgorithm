class Solution:
	def climbStairs(self,n):
		if n==1:
			return 1;
		elif n==2:
			return 2;
		else:
			return self.climbStairs(n-1)+self.climbStairs(n-2);


Test = Solution()
print(Test.climbStairs(15))


# 这里是使用递归版本的内容来实现。青蛙跳台阶的部分。




