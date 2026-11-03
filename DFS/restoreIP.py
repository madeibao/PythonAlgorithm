
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s, 0, [], res)
        return res

    def dfs(self, s: str, start: int, path: List[str], res: List[str]):
        if len(path) == 4:
            if start == len(s):
                res.append('.'.join(path))
            return

        for length in range(1, 4):
            if start + length > len(s):
                break
            segment = s[start:start + length]
            if not self.validIP(segment):
                continue
            self.dfs(s, start + length, path + [segment], res)

    def validIP(self, segment: str) -> bool:
        if len(segment) > 1 and segment[0] == '0':
            return False
        if int(segment) > 255 or int(segment) < 0:
            return False
        return True

if __name__ == "__main__":
    s = "25525511135"
    solution = Solution()
    print(solution.restoreIpAddresses(s))

