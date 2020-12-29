



from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                ans.append(nums[i])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicates([4,3,2,7,8,2,3,1]))




















