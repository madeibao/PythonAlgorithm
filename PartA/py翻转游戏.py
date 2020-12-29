

# python的翻转的游戏。


class Solution():
    def flipGame(self, s):
        result = []
        for i in range(len(s)):
            if s[i:i + 2] == "++":
                result.append(s[:i] + "--" + s[i + 2:])
        return result


if __name__ == "__main__":
    s = Solution()
    str2 = "++++"
    print(s.flipGame(str2))

