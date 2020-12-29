


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        def back(chosen, cur):
            res.append(cur)
            if not chosen:
                return
            for i in range(len(chosen)):
                back(chosen[i + 1:], cur + [chosen[i]])  # chosen[i + 1:]不会越界

        res = []
        back(nums, [])
        return res


if __name__ == "__main__": 
	s= Solution()
	list2 = [1,2,3]
	print(s.subsets(list2))

