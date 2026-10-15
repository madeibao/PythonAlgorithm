


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        ans = 0
        count = 0
        for num in nums:
            if count == 0:
                ans = num
            count += (1 if ans == num else -1)
        return ans

if __name__ == "__main__":
    nums = [3,2,3]
    print(Solution().majorityElement(nums))