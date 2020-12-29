

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return (A+A).find(B)!=-1 and len(A)==len(B)


if __name__ == "__main__":
    s = Solution()
    str2 = "abcde"
    str3 = "deabc"
    print(s.rotateString(str2, str3))

