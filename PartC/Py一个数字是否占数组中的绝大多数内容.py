

# 给出一个按 非递减 顺序排列的数组 nums，和一个目标数值 target。
# 假如数组 nums 中绝大多数元素的数值都等于 target，则返回 True，否则请返回 False。
# 所谓占绝大多数，是指在长度为 N 的数组中出现必须 超过 N/2 次。


from typing import List
import collections


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        print(collections.Counter(nums))
        return collections.Counter(nums)[target] > len(nums)/2


if __name__ == "__main__":
    s = Solution()
    nums = [2,4,5,5,5,5,5,6,6]
    print(s.isMajorityElement(nums, 5))









