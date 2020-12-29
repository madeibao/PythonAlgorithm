


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word[0]>= 'A' and word[0]<='Z' and word[1:].islower():
            return True
        else:
            return False



if __name__ == "__main__":
    s = Solution()
    str2 ="Google"
    print(s.detectCapitalUse(str2))

