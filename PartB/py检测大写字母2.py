


# 三中条件条件符合，
# 首字母大写，
# 全部大写，
# 全部小写。


class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if word.isupper():
            return True
        elif word.islower():
            return True
        elif 'A'<= word[0] <= 'Z' and word[1:].isLower():
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.detectCapitalUse("leetcode"))







