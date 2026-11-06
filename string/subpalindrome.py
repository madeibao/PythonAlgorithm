

class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left: int, right: int) -> int:
            cnt = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
            return cnt

        res = 0
        n = len(s)
        for i in range(n):
            # 奇数中心
            res += expand(i, i)
            # 偶数中心
            res += expand(i, i + 1)
        return res

if __name__ == "__main__":
    sol = Solution()
    for case in ("abc", "aaa", "a", "ab", "racecar"):
        print(f"{case!r} -> {sol.countSubstrings(case)}")

