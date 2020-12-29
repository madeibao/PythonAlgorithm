



# leetcode，放置最多水的容器结果值。



class Solution(object):
    def maxArea(self,nums):
        i, j, res = 0, len(nums)-1, 0

        while i < j:
            if nums[i]<nums[j]:
                res = max(res,nums[i]*(j-i))
                i+=1
            else:
                res = max(res,nums[j]*(j-i))
                j-=1

        return res  

if __name__ == "__main__":
    s =Solution()
    list2 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(s.maxArea(list2))

