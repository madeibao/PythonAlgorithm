

class Solution:
    def frequencySort(self, s: str) -> str:
        # Counter
        return ''.join([i * j for i, j in collections.Counter(s).most_common()])


if __name__ == '__main__':
	s = Solution()
	print(s.frequencySort("leetcode"))
	