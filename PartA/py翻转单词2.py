

class Solution:
    def reverseWords(self, s: str) -> str:
        list2 = s.split(" ")[::-1]
        return " ".join(list2)


if __name__ == "__main__":
    s = Solution()
    str2 ="the sky is blue"
    print(s.reverseWords(str2))

