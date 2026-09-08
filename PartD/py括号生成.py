from typing import List


class Solution:
    def __init__(self):
        self.res = None

    def generate(self, n: int) -> List[str]:
        self.res: List[str] = []
        def helper(str2: str, left: int, right: int) -> None:
            if left > right:
                return
            if left < 0 or right < 0:
                return
            if left == 0 and right == 0:
                self.res.append(str2)
                return
            helper(str2 + "(", left - 1, right)
            helper(str2 + ")", left, right - 1)

        helper("", n, n)
        return self.res


if __name__ == '__main__':
    s = Solution()
    n: int = 3
    print(s.generate(n))
