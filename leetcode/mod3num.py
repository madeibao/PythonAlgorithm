
class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        
        s = sum(nums)
        moda = []
        modb = []

        for i in range(len(nums)):
            if nums[i]%3==1:
                moda.append(nums[i])
            elif nums[i]%3==2:
                modb.append(nums[i])
        
        moda.sort()
        modb.sort()

        if s%3==0:
            return s

        res = []
        if s%3==1:
            if len(moda) >=1:
                res.append(s-moda[0])
            if len(modb) >=2:
                res.append(s-modb[0]-modb[1])
        
        if s%3==2:
            if len(modb)>=1:
                res.append(s-modb[0])
            if len(moda)>=2:
                res.append(s-moda[0]-moda[1])
        return max(res) if res else 0


if __name__=="__main__":
    nums = [3,6,5,1,8]
    s = Solution()
    print(s.maxSumDivThree(nums))