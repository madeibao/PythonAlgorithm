

# 这里是回溯解法，更简洁优雅。

from typing import List

class Solution:
    def validIp(self, t: str) -> bool:
            if not t:
                return False
            if (len(t) > 4) or (len(t) > 1 and t[0] == "0"):
                return False
            num = int(t)
            return num <= 255 and num >= 0

    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def dfs(s, path):
            if len(path) == 4:
                if not s:
                    ans.append(".".join(path))
                return
            for i in range(1, 4):
                if i <= len(s):
                    t = s[:i]
                    if self.validIp(t):
                        dfs(s[i:], path + [t])
        dfs(s, [])
        return ans

if __name__ == "__main__":
    s = "25525511135"
    solution = Solution()
    print(solution.restoreIpAddresses(s))
