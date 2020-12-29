# -*- coding: utf-8 -*-


from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:


            return False
        a = A.index(max(A))

        if a == 0 or a == len(A) - 1:
            return False

        # 最大的指针的前面的位置内容。
        for i in range(a):
            if A[i] >= A[i+1]:
                return False

        # 最大的指针的后面的
        for i in range(a,len(A)-1):
            if A[i] <= A[i+1]:
                return False
        return True


if __name__ == "__main__": 
    s = Solution()
    print(s.validMountainArray([0,3,2,1]))


    