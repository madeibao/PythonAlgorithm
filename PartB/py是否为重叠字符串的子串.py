

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:

        i = 1
        while i < len(A):
            if (A*i).find(B)!=-1:
                return i
            i+=1

        return -1


if __name__ == "__main__":
    s = Solution()
    A = "abcd"
    B = "cdabcdab"。
    print(s.repeatedStringMatch(A,B))
