
from typing import List, Tuple


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:

        def isSubsequence(s: str, t: str) -> bool:
            s = list(s)
            for _t in t:
                if not s:
                    return True
                if _t == s[0]:
                    s.pop(0)
            return len(s) == 0

        count = 0
        for i in words:
            if isSubsequence(i, S):
                count +=1
        return count


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        count=0
        for i in words:
            num=0
            pos=-1
            for j in i:
                pos=S.find(j,pos+1)
                if pos==-1:
                    break
                else:
                    num=num+1
            if num==len(i):
                count=count+1
                
        # 返回最终的结果值.
        return count
                

                


if __name__ == "__main__":
    s = Solution()

    S2 = "abcde"
    words = ["a", "bb", "acd", "ace"]
    print(s.numMatchingSubseq(S2, words))

