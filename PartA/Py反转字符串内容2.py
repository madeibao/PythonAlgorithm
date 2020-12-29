

class Solution():
    def reverseString(self,s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right],s[left]
                helper(left + 1, right-1)
        helper(0, len(s) - 1)
        return s


if __name__ == "__main__":
    s = Solution()
    print(s.reverseString(["h","e","l","l","o"]))
















