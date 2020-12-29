
在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。
给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

示例 1:

输入: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
输出: 
[[1,2,3,4]]
解释:
行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
#=============================================================================================



from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        list3 = [[0 for i in range(c)] for i in range(r)]
        if len(list3)*len(list3[0])!=len(nums)*len(nums[0]):   # 如果行列值不相等的情况下，就返回原来的矩阵形式。
            return nums
        else:
            list2 = []
            list3 = []
            for i in range(len(nums)):
                list2 += nums[i]    # 把原来的矩阵变成一行的形式来进行存储。 
            #   list2.extend(nums[i])
            for i in range(0,len(list2),c):
                list3.append(list2[i:i+c]) # 每次截取其中的一个列表的内容。
            return list3   # 返回最终的结果值。


if __name__ == '__main__':
    s = Solution()
    nums = [[1, 2],[3, 4]]
    print(s.matrixReshape(nums, 1, 4))








