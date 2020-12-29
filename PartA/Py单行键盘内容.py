


# 打印时需要移动的位置的总和。
class Solution():
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {}

        # 首先是建立一个字典的内容。
        for key, value in enumerate(keyboard):
            d[value] = key
        
        res,pre = 0,0
        for c in word:
            res += abs(d[c] - pre)
            pre = d[c]
        return res


if __name__ == "__main__":
    s = Solution()
    keyboard = "pqrstuvwxyzabcdefghijklmno"
    word = "leetcode"
    print(s.calculateTime(keyboard, word))







