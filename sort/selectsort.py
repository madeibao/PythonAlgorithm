
from typing import List

class Solution:
    def selectSort(self, nums:List[int])->List[int]:
        for i in range(len(nums)):
            minIndex = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[minIndex]:
                    minIndex = j
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.selectSort([3, 2, 1]))
    print(s.selectSort([1, 3,2,5,4,7,10,9,8, 6]))