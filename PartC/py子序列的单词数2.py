

from typing import List,Tuple


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:

        count = 0
        for i in words:
            pos = -1
            num = 0
            for j in i:
                pos = S.find(j, pos+1)
                if pos == -1:
                    break
                else:
                    num +=1
            if num == len(i):
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    S = "abcde"
    words = ["a", "bb", "acd", "ace"]
    print(s.numMatchingSubseq(S, words))

    
    