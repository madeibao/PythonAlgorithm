# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

# 示例 :

# 输入: [1,2,1,3,2,5]
# 输出: [3,5]


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        return [key for key,value in d.items() if value==1]

if __name__ == "__main__":
	s = Solution()
	print(s.singleNumber([1,2,1,3,2,5]))