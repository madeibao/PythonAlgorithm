from typing import List

class Solution:
    def validIP(self, segment: str) -> bool:
        if not segment: return False
        if len(segment) > 3:
            return False
        if len(segment) > 1 and segment[0] == '0':
            return False
        if int(segment) > 255 or int(segment) < 0:
            return False
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def dfs(s: str, path: List[str]):
            if len(path) == 4:
                if not s:
                    ans.append('.'.join(path))
                return
            for i in range(1, 4):
                if i <= len(s):
                    segment = s[:i]
                    if self.validIP(segment):
                        dfs(s[i:], path + [segment])
        dfs(s, [])
        return ans

if __name__ == "__main__":
    s = "25525511135"
    solution = Solution()
    print(solution.restoreIpAddresses(s))

