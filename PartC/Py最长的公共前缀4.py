
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""
        for i in zip(*strs):
            if len(set(i))==1:
                res+=i[0]
            else:
            	break
        return res


if __name__ == "__main__":
    s =Solution()
    list2 = ["flower","flow","flight"]
    print(s.longestCommonPrefix(list2))

