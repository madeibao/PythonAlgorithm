


from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
		
		def inter(stra, strb):
			if list(set(stra)&set(strb))==[]
				return True
			return False

		res = 0

		for i in range(len(words)-1):
			for j in range(i+1, len(words)):
				if inter(words[i], words[j]:
					res = max(res,len(words[i])*len(words[j]))
				else:
					continue
		return 0




if __name__ == "__main__":
	s = Solution()
	list2 = ["abcw","baz","foo","bar","xtfn","abcdef"]
	print(s.maxProduct(list2))
