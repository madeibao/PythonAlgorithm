
from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res = []
        length = len(s)

        def backtrack(start:int, path:str):
            if start == length:
                res.append(path)
                return
            if s[start].isalpha():
                backtrack(start + 1, path + s[start].lower())
                backtrack(start + 1, path + s[start].upper())
            else:
                backtrack(start + 1, path + s[start])

        backtrack(0, "")
        return res

if __name__ == "__main__":
    solution = Solution()
    s = "a1b2"
    print(solution.letterCasePermutation(s))