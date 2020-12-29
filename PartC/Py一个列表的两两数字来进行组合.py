

import itertools


def getlist2(nums):
	list2 = list(itertools.combinations(nums, 2))
	return list2



print(getlist2([1, 2, 3]))

[(1, 2), (1, 3), (2, 3)]