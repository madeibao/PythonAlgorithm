给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：


	A.length >= 3
	在 0 < i < A.length - 1 条件下，存在 i 使得：
	
		A[0] < A[1] < ... A[i-1] < A[i] 
		A[i] > A[i+1] > ... > A[B.length - 1]

示例 1：

输入：[2,1]
输出：false


示例 2：

输入：[3,5,5]
输出：false


示例 3：

输入：[0,3,2,1]
输出：true

#============================================================================

from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        def isMonotonic(A) -> bool:
            if sorted(A) == A and len(set(A)) == len(A):
                return True
            elif sorted(A) == A[::-1] and len(set(A)) == len(A):
                return True
            else:
                return False

        if len(A) == 0: return False
        num2 = max(A)
        if A.index(num2) == 0 or A.index(num2) == len(A)-1:
            return False
        else:
            num3 = A[:A.index(num2)+1]
            num4 = A[A.index(num2):]
            if isMonotonic(num3) and isMonotonic(num4):
                return True
            else:
                return False


if __name__ == '__main__':
    s = Solution()
    print(s.validMountainArray([0, 3, 2, 1]))

