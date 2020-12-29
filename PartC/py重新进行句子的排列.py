



class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower() # 首字母转小写
        text = text.split(" ") # 通过 空格 分割成数组
        text.sort(key=lambda x: len(x)) # 使用 lambda 按照元素长度排序
        return ' '.join(text).capitalize() # 最后首字母大写

if __name__ == "__main__":
    s  = Solution()
    text = "Leetcode is cool"
    print(s.arrangeWords(text))
