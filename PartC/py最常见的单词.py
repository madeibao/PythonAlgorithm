import collections
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        l = (paragraph.replace(',', ' ').replace('.', '')
             .replace('!', '').replace('?', '').replace(';', '').replace("'", '').lower())
        a = l.split()
        for i in a:
            if i in banned:
                a.remove(i)
        c = collections.Counter(a)
        res = ""
        for k, v in c.items():
            if v == max(c.values()):
                res = k
        return res


if __name__ == "__main__":
    s = Solution()

    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    print(s.mostCommonWord(paragraph, banned))
