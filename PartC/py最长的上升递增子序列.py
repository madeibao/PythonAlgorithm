


class Solution():
    def length(self,nums):
        n = len(nums)
        if n==0:
            return 0 
        
        dp= [1]*n

        ans =1
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                ans = max(ans,dp[i])
        return ans

if __name__ == "__main__":
    s =Solution()
    list2= [10,9,2,5,3,7,101,18]
    print(s.length(list2))

    