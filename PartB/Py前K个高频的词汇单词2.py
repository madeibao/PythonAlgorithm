

from collections import Counter


class Solution():
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic2 = dict(Counter(nums))
        sort = sorted(dic2.items(), key=lambda e: e[1], reverse=True)	
        res = []
        for i in range(k):
            res.append(sort[i][0])
        return res


if __name__ == "__main__":
	S = Solution()
	nums = [1,1,1,2,2,3]
	k = 2

	print(s.topKFrequent(nums, k))

