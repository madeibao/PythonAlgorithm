给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true

示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true

示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false




from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = {}    # 字典的键是不重复的内容。
        # 没有重复元素, 肯定返回False
        if len(set(nums)) == len(nums): return False
        # 只要有一个重复元素 相差的索引号 <=k 返回True
        for idx, num in enumerate(nums):
            if num in lookup and idx - lookup[num] <= k:   # 只要后面出现数字，由于字典的键具有唯一性。并且两者的位置差值小于等于k。
                return True
            lookup[num] = idx

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))