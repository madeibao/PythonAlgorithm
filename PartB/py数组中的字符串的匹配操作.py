


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        for i in words:
            for j in words:
                if i in j and i!=j:
                    res.append(i)
        return list(set(res))

if __name__ == "__main__":
	s = Solution()
	words = ["leetcode", "et","code"]
	print(s.stringMatching(words))

