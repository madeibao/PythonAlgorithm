
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    for d in range(1, 4):
                        if a + b + c + d == len(s):
                            t = s[:a]
                            u = s[a : a + b]
                            v = s[a + b : a + b + c]
                            w = s[a + b + c :a + b + c + d]
                            if (
                                self.validIp(t)
                                and self.validIp(u)
                                and self.validIp(v)
                                and self.validIp(w)
                            ):
                                ans.append(".".join([t, u, v, w]))
        return ans

    def validIp(self, t: str) -> bool:
        if (len(t) > 4) or (len(t) > 1 and t[0] == "0"):
            return False
        num = int(t)
        return num <= 255 and num >= 0

if __name__ == "__main__":
    s = "25525511135"
    solution = Solution()
    print(solution.restoreIpAddresses(s))
    # Output: ["255.255.11.135","255.255.111.35"]
