


class Solution:
    def reverseLeftWords(self, s: str, k: int) -> str:
        n = len(s)
        s = s + s
        return s[k:n + k]


if __name__ == "__main__":
	s  = Solution().reverseLeftWords("abcdefg", 2)


	#------------------------------------------------------------------------------------------------