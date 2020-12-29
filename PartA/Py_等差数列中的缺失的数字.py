


# 给定一个等差数列的内容，求出等差数列中的缺失的数字。

# from typing import List
from typing import List


class Solution():
    def missingNumber(self, A: List[int]) -> int:
        return (A[0] + A[-1]) *(len(A)+1)//2 - sum(A)


# if __name__ == "__main__":
#     arr = [1, 5, 7, 9, 11,]
#     s =Solution()  
#     print(s.missingNumber(arr))

 

if __name__ == "__main__":
	s  = Solution()
	print(s.missingNumber([0,1,3,4,5,6,7]))