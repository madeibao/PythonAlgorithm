

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        length = len(nums)
        nums.sort()  # Sort the numbers to handle duplicates

        def backtrack(start):
            if start == length:
                res.append(nums.copy())
                return
            for i in range(start, length):
                # Skip duplicates
                if i > start and nums[i] == nums[start]:
                    continue
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 2]
    print(solution.permuteUnique(nums))

    