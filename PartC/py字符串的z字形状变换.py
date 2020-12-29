
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        # flag用来进行表示是否调转位置。
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)


if __name__ == "__main__":
    s = Solution()
    print(s.convert("LEETCODEISHIRING", 3))

