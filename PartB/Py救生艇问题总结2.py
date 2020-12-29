

class Solution():
    def boat(self,nums,k):
        i,j = 0, len(nums)-1
        ans = 0
        while i<j:
            ans +=1
            if nums[i]+nums[j]<=k:
                i+=1
            j-=1

        return ans


if __name__ == "__main__":
    list2 = [1,2,3]
    limit = 3

    s = Solution()
    print(s.boat(list2,limit))


