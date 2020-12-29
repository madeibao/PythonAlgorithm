

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
    	res = []
    	i = 0, j = n

    	while i < n and j < len(nums):
    		res.append(nums[i])
    		res.append(nums[j])
    		i+=1
    		j+=1

    	return res


if __name__ == "__main__":
	s = Solution()
	nums = [1,2,3,4,4,3,2,1]
	n = 4
	print(s.shuffle(nums, n))



