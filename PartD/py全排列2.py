




class Solution(object):
    def permutations(self,nums):
        if not nums:
            return []

        res= []
        def helper(start):
            if start==len(nums):
                res.append(nums[:])
            for i in range(start,len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                helper(start+1)
                nums[i], nums[start]  = nums[start] , nums[i]
        helper(0)
        return res

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    print(s.permutations(nums))

