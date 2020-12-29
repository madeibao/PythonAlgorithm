给定一个不重复的数组元素[2, 3, 5]
然后和一个目标值 8

然后给出多少种组合得出列表的总和为8.

例如[2, 2, 2, 2]
列表元素内容可以重复的进行表示

class Solution():
    def getSum(self, nums, target):
        nums.sort()
        N = len(nums)
        temp_sum = 0

        res = []
        def helper(i, temp_sum, sumnumber):
            if temp_sum>target or i == N:
                return 
            
            if temp_sum == target:
                res.append(sumnumber)
                return

            helper(i, temp_sum + nums[i], sumnumber+ [nums[i]])
            helper(i+1, temp_sum, sumnumber)

        helper(0,0,[])

        return res

if __name__ == "__main__":
    nums = [2, 3, 5]
    target = 8
    s = Solution()
    print(s.getSum(nums, target))



