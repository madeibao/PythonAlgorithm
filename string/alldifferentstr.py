

from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        p_count = [0] * 26
        s_count = [0] * 26
        for i in range(len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1
        res = []
        if s_count == p_count:
            res.append(0)
        for i in range(len(p), len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            if s_count == p_count:
                res.append(i - len(p) + 1)
        return res

if __name__ == '__main__':
    print(Solution().findAnagrams("cbaebabacd", "abc"))

    