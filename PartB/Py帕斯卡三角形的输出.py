from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex+1):
            res.append([1])
            for j in range(1, i + 1):
                if j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i - 1][j - 1] + res[i - 1][j])
        return res[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(3))




