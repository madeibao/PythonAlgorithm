


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target-x in dict:
                return (dict[target-x],i)
            dict[x] = i


if __name__ == "__main__":
    s = Solution()
    list2 = [2, 7, 10, 3, 3, 2, 8]
    k = 9
    print(s.twoSum(list2, k))






