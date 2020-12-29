



给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。

示例 1:

输入: [1,4,3,2]

输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).




from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        list2 = sorted(nums)

        list3 = []
        for i in range(0, len(list2)-1, 2):
            list3.append((list2[i], list2[i+1]))

        sum3 = 0
        for i in list3:
            sum3 += min(i[0], i[1])

        return sum3


if __name__ == '__main__':
    s = Solution()
    print(s.arrayPairSum([1, 4, 3, 2]))