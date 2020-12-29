
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        setA = set([path[0] for path in paths])
        setB = set([path[1] for path in paths])
        res = setB-setA
        return list(res)[0]

if __name__ == "__main__":
    s =Solution()
    paths = [["B","C"],["D","B"],["C","A"]]
    print(s.destCity(paths))

    