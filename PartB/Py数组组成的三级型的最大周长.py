from typing import List

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        nums = sorted(A)

        temp = 0    
        # range循环内容包括开始，但是不包括结尾内容。
        for i in range(len(nums)-1,1, -1):
            a = nums[i]
            b = nums[i-1]
            c = nums[i-2]    
            if a<b+c:
                temp=a+b+c
                break
        if temp!= 0:
            return temp
        else:
            return 0

if __name__=='__main__':
    s = Solution()
    print(s.largestPerimeter([2,1,2]))