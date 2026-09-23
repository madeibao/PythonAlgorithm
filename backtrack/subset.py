
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        length = len(nums)

        def back(start, path):
            res.append(path.copy())
            for i in range(start, length):
                back(i + 1, path + [nums[i]])

        back(0, [])
        return res

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.subsets(nums))

# 这里面内容有重复的内容



