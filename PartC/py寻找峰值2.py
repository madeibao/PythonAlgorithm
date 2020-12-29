

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return righ


if __name__ == "__main__":
	s = Solution()
	list2 = [1,2,1,3,5,6,4]
	print(s.findPeakElement(list2))

	