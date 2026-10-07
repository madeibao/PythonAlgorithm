
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        p = sorted(p)
        res = []
        for i in range(len(s) - len(p) + 1):
            if sorted(s[i:i + len(p)]) == p:
                res.append(i)
        return res

if __name__ == '__main__':
    print(Solution().findAnagrams("cbaebabacd", "abc"))
