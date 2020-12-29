


class Solution():
    def removeDuplicates(self, nums):
        i= 0
        while i < len(nums)-1:
            if nums[i]== nums[i+1]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1,1,2]))














