



class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s = str.split()
        return len(set(zip(pattern, s))) == len(set(s)) == len(set(pattern))  and len(pattern) == len(s) 




if __name__ == "__main__":
	s2 ="abba"
	str2 = "dog cat cat dog"

	s3 = Solution()
	print(s3.wordPattern(s2, str2))

