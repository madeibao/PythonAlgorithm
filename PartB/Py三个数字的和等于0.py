
# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums_hash = {}
#         result = list()
#         for num in nums:
#             nums_hash[num] = nums_hash.get(num, 0) + 1
#         # 首先用字典来建立一个统计的结果值。
#         if 0 in nums_hash and nums_hash[0] >= 3:
#             result.append([0, 0, 0])

#         nums = sorted(list(nums_hash.keys()))

#         for i, num in enumerate(nums):
#             for j in nums[i+1:]:
#                 if num*2 + j == 0 and nums_hash[num] >= 2:
#                     result.append([num, num, j])
#                 if j*2 + num == 0 and nums_hash[j] >= 2:
#                     result.append([j, j, num])
                
#                 dif = 0 - num - j

#                 if dif > j and dif in nums_hash:
#                     result.append([num, j, dif])                
#         return result


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from collections import Counter
        k = []
        result = []
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + 1:]):
                for _, c in enumerate(nums[j + i + 2:]):
                    if a + b + c == 0 and Counter([a, b, c]) not in k:
                        k.append(Counter([a, b, c]))

        
        for i in k:
            result.append(list(i.elements()))
        return result



if __name__=="__main__":
	s = Solution()
	nums = [-1, 0, 1, 2, -1, -4]
	print(s.threeSum(nums))


