

from typing import List



class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ans=sorted(list(set(nums)))
        return ans[-3] if len(ans)>2 else ans[-1]


if __name__ == "__main__":
	s = Solution()
	list2 = [2,3,1]
	print(s.thirdMax(list2))

