
import itertools

class Solution():
    def getSubSets(self,nums):
        res = []
        N = len(nums)
        for i in range(N+1):
            for temp in itertools.permutations(nums, i):
                res.append(list(temp))
        return res

if __name__ == "__main__":
    s =Solution()   
    print(s.getSubSets([2, 3, 4]))


# [[], [2], [3], [4], [2, 3], [2, 4], [3, 2], [3, 4], [4, 2], [4, 3], [2, 3, 4], [2, 4, 3], [3, 2, 4], [3, 4, 2], [4, 2, 3], [4, 3, 2]]
# 以上的调用库函数的方法内容来实现。


class Solution():
    def getSubSets(self, nums):
        if not nums:
            return []
        res = []
        N = len(nums)

        def helper(idx, temp_list):
            res.append(temp_list)

            for i in range(idx, N):
                helper(i+1, temp_list+[nums[i]])
        helper(0, [])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.getSubSets([2, 3, 4]))


# [[], [2], [2, 3], [2, 3, 4], [2, 4], [3], [3, 4], [4]]










