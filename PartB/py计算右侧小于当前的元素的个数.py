


from typing import List
# import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
    	res = []

    	sorted_nums = []

    	for i in range(len(nums)-1,-1,-1):
    		index = bisect.bisect_left(sorted_nums,nums[i] )
    		res.append(index)
    		sorted_nums.insert(index,nums[i])

    	return res[::-1]


if __name__ == "__main__":
	s =Solution()
	list2 = [5,2,6,1]
	print(s.countSmaller(list2))

