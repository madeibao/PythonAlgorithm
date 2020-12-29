

class Solution(object):
    def reverseWords(self, string):
        """
        :type str: List[str]
        :rtype: None Do not return anything, modify str in-place instead.
        """
        string[:] = list(" ".join("".join(string).split(" ")[::-1]))
        return string

if __name__ == "__main__":
    s = Solution()
    list2 = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
    print(s.reverseWords(list2))

