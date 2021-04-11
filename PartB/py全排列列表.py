
from typing import List

class Solution(object):
    def permute3(self, nums: List[int]) -> List[List[int]]:
        """回溯的另一种写法"""
        res = []
        length = len(nums)
        def _backtrack(start=0):
            if start == length:
                # nums[:] 返回 nums 的一个副本，指向新的引用，这样后续的操作不会影响已经已知解
                res.append(nums[:])
            for i in range(start, length):
                nums[start], nums[i] = nums[i], nums[start]
                _backtrack(start+1)
                nums[start], nums[i] = nums[i], nums[start]
        _backtrack()
        return res

if __name__ == "__main__":
	s =Solution()
	list2 =[1,2,3]
	print(s.permute3(list2))


# 最简单的写法来实现列表的全排列的


class Solution(object):
	def permute3(self,nums):

		res = []
		length = len(nums)

		def helper(start):
			if start==length:
				res.append(nums[:])
			for i in range(start, length):
				nums[i], nums[start] = nums[start], nums[i]
				helper(start+1)
				nums[i], nums[start] = nums[start], nums[i]
			return res


if __name__ == "__main__":
	s =Solution()
	nums = [1,2,3]
	print(s.permute3(nums))

#------------------------------------------------------------------------------------------------#
# 方法3的结果值
from typing import List


class Solution():
    def permute2(self, nums: List[int]) -> List[List[int]]:
        """自己写回溯法"""
        res = []

        def _backtrace(nums, pre_list):
            if len(nums) <= 0:
                res.append(pre_list)
            else:
                for i in nums:
                    # 注意copy一份新的调用，否则无法正常循环
                    p_list = pre_list.copy()
                    p_list.append(i)
                    left_nums = nums.copy()
                    left_nums.remove(i)
                    _backtrace(left_nums, p_list)

        _backtrace(nums, [])
        return res


if __name__ == '__main__':
    s = Solution()
    list2 = [1, 2, 3]
    print(s.permute2(list2))



class Solution(object):
    def permutate(self, nums):

        res = []
        def helper(start):
            if start == len(nums):
                res.append(nums[:])
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                helper(start + 1)
                nums[i], nums[start] = nums[start], nums[i]
        helper(0)
        return res


if __name__ == "__main__":
    s = Solution()
    list2 = [1, 2, 3]
    print(s.permutate(list2))


# --------------------------------------------------------------------------------------------------------------------

from typing import List


class Solution(object):
    def path2(self, nums):
        def helper(nums, depth, size, path, visited, res):
            if depth ==size:
                res.append(path.copy())
            for i in range(size):
                if not visited[i]:
                    # 如果是重复的内容，那么就直接的跳过去执行。
                    if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                        continue
                    visited[i] = True
                    path.append(nums[i])
                    helper(nums, depth+1, size, path, visited, res)
                    visited[i] = False
                    path.pop()

        nums.sort()
        if len(nums) == 0:
            return []
        res = []
        size = len(nums)
        visited = [False for _ in range(size)]
        helper(nums, 0, size, [], visited, res)
        return res


if __name__ == '__main__':
    s = Solution()
    list2 = [1, 2, 2]
    print(s.path2(list2))




