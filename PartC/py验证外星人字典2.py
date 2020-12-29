



class Solution():
	def isAlienSorted(self,words,order):

		if not words:
			return False

		if len(order)!=26:
			return False
		temp = {}
		for i in range(26):
			temp[order[i]] = chr(ord('a')+i)

		newWords = []
		for word in words:
			t = []
			for j in word:
				t.append(temp[j])
			newWords.append("".join(t))

		for i in range(1,len(newWords)):
			if newWords[i]<newWords[i-1]:
				return False
		return True


if __name__ == "__main__":
	s =Solution()
	words = ["hello","leetcode"]
	order = "hlabcdefgijkmnopqrstuvwxyz"
	print(s.isAlienSorted(words, order))



