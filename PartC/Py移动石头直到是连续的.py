


# 移动石头变成连续的。

from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
    	a, b,c = sorted([a,b,c])
    	if b-a==1 and c-b==1: return [0, 0]
    	return [1, if b - a <= 2 or c - b  <= 2 else 2, c-a-2]


if __name__ == "__main__":
	s = Solution()
	list2 =[2,3,4]
	print(s.numMovesStones(list2))
