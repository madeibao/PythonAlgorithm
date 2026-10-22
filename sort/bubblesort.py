
from typing import List
class Solution:
    def bubbleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums


class Solution2:
    def bubbleSort(self, nums: List[int]) -> List[int]:

        n = len(nums)
        for i in range(n - 1):
            swapped = False
            # 相邻比较，每轮把最大值冒到末尾
            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:      # 本轮无交换，已有序
                break
        return nums 


if __name__ == '__main__':
    s = Solution()
    print(s.bubbleSort([3, 2, 1]))

    print(Solution2().bubbleSort([3, 2, 1]))


