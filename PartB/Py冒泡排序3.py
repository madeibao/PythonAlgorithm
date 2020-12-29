



class Solution():
    def bubble(self, nums):

        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[i]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp

        return nums


if __name__ == "__main__":
    s = Solution()
    list2 = [23, 3, 2, 4, 5, 6, 4, 6, 43, 2, 4, 56]
    print(s.bubble(list2))

