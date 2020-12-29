

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t) and len(set(s)) != len(set(t)) :return False

        if len(set(zip(s,t))) == len(set(s)):
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic("abb","cdd"))