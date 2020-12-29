



class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in range(len(letters)):
            if ord(letters[i]) > ord(target):
                return letters[i]
        return letters[0]


if __name__ == "__main__":
	s = Solution()
	letters = ['c','f','j']
	target = 'a'
	print(s.nextGreatestLetter(letters,target))

	