

from typing import List

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        print(list(zip(*A)))
        return [list(lows) for lows in list(zip(*A))]


if __name__ == '__main__':

    s = Solution()
    list2 = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    print(s.transpose(list2))






