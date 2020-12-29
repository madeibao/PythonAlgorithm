集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。

给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1:

输入: nums = [1,2,2,4]
输出: [2,3]


from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = dict()
        list2 = []
        for i in nums:
            counts[i] = counts.get(i, 0) + 1

        temp = 0
        for key in counts:
            if counts[key]==2:
                list2.append(key)
                temp = key

        temp2 = len(nums) * (len(nums) + 1) // 2
        nums.remove(temp)
        list2.append(temp2-sum(nums))
        return list2


if __name__ == '__main__':
    s = Solution()
    print(s.findErrorNums([1,2,2,4]))


#--------------------------------------------------------------------
别人的更加精巧的解题方法:


class Solution:
    def findErrorNums(self, nums: list) -> list:
       err = sum(nums) - sum(set(nums))
       re = set(range(1,len(nums) +1) - set(nums))
       return [err,re.pop()]

























