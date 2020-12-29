


# 求X的平方根。

class Solution(object):
	def mySqrt(self,x)->int:

		return int(x**0.5)	



class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while(1):
            mid = left + (right - left) // 2
            if(mid * mid == x):
                return mid
            elif(mid * mid > x):
                right = mid
            else:
                left = mid + 1
                if(left * left > x):
                    return mid


if __name__ == "__main":
	s =Solution()
	print(s.mySqrt(15))
