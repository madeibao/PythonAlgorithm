

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s)):
            print(dp)
            if dp[i] == True:
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in wordDict:
                        dp[j] = True
        # 观察是否能够跳到最后的值。
        return dp[-1]

#------------------------------------------------------------------
#----------------------------------------------------------------------------
# 另一种解法。


class Solution():
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        if s in wordDict: return True
        for i in range(1, len(s) + 1):
            # 从第一个到最后一个字符
            for j in range(i):
                # i之前的第一个到i个字符
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]


if __name__ == '__main__':
    s = Solution()
    s2 = "applepenapple"
    wordDict = ["apple", "pen"]
    print(s.wordBreak(s2, wordDict))