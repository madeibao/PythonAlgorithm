

# # 矩阵的右上角的位置沿着对角线来打印

# 题目描述
# 有一个二维数组(n*n),写程序实现从右上角到左下角沿主对角线方向打印。

# 给定一个二位数组arr及题目中的参数n，请返回结果数组。

# 测试样例：
# [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],4
# 返回：[4,3,8,2,7,12,1,6,11,16,5,10,15,9,14,13]
#------------------------------------------------------------------------------------------------

from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        '''
        5394. 对角线遍历 II
        :param nums:
        :return:
        '''
        num_list = []
        for i in range(len(nums)-1, -1, -1):
            for j in range(len(nums[i])):
                num_list.append((i-j, j, nums[i][j]))

        num_list.sort()
        return [i[2] for i in num_list]


if __name__ == '__main__':
    s = Solution()
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(s.findDiagonalOrder(nums))


# 下面的是另一个问题的解法：

# 给你一个列表 nums ，里面每一个元素都是一个整数列表。请你依照下面各图的规则，按顺序返回 nums 中对角线上的整数。
# leetcode 1424


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:    
        
        '''
        5394. 对角线遍历 II
        :param nums:
        :return:
        '''
        num_list = []
        for i in range(len(nums)):
            for j in range(len(nums[i])-1, -1, -1):
                num_list.append((i + j, j, nums[i][j]))

        num_list.sort()
        return [i[2] for i in num_list]
