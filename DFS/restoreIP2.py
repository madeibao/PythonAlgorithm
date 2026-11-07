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
                        # 下面的path+[segment]是关键，因为path是引用传递的，不加[]会出错,
                        # 这里的path+[segment]是创建了一个新的列表，避免了引用传递的问题
                        dfs(s[i:], path + [segment])
        dfs(s, [])
        return ans


    def restoreIpAddresses2(self, s: str) -> List[str]:
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
                        path.append(segment)
                        dfs(s[i:], path)
                        path.pop()  # 回溯, 非常重要，否则会出错

        dfs(s, [])
        return ans

if __name__ == "__main__":
    s = "25525511135"
    solution = Solution()
    print(solution.restoreIpAddresses2(s))

