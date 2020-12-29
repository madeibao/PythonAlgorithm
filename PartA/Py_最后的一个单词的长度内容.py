


class Solution(object):

    def lengthOfLastWord(self, s):

        """

        :type s: str
        :rtype: int

        """
        return len(s.split()[-1]) if s.split() else 0


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("hello world"))

