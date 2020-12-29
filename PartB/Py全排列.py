
from typing import List
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
    
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]


# 另一种方式的全排列


from typing import List
import itertools    # 设置迭代器的内容。


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0:
            return []

        res = []
        self.__helper(nums, 0, size, res)
        return res

    def __helper(self, nums, begin, size, res):
        if begin == size - 1:
            # 打开注释，看看程序是如何运行的
            # print('调试：', nums)
            res.append(nums.copy())
            return
        self.__helper(nums, begin + 1, size, res)
        # 从 begin 的下一位开始一直要交换到最后一位
        for index in range(begin + 1, size):
            nums[begin], nums[index] = nums[index], nums[begin]
            self.__helper(nums, begin + 1, size, res)
            # 注意：递归完成以后要交换回来
            nums[begin], nums[index] = nums[index], nums[begin]


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))




# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

