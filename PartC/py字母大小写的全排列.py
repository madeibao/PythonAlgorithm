
from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []

        def helper(s, tmp):
            if not s:
                ans.append(''.join(tmp))
                return
            if s[0].isalpha():
                helper(s[1:], tmp + [s[0].upper()])
                helper(s[1:], tmp + [s[0].lower()])
            else:
                helper(s[1:], tmp + [s[0]])

        helper(S, [])
        return ans


if __name__ == "__main__":
    s = Solution()

    list2 = "a2b3"
    print(s.letterCasePermutation(list2))
