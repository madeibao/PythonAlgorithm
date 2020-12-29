
'''
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
'''

#============================================================================================================


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        one, two = set(), set()
        for num in nums:
            # 第一次出现，放入one集合中
            if num not in one:
                one.add(num)
            # 不是第一次出现，则放入two集合中
            else:
                two.add(num)
        # 至少出现一次的集合one - 出现两次及以上的集合two
        return list(one-two)


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1, 2, 1, 3, 2, 5]))

