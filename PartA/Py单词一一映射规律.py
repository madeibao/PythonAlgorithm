给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true

示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false

示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false

示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
#----------------------------------------------------------------------------------------

class Solution():
    def wordPattern(self, pattern, str):
        a = str.split(" ")
        b = list(pattern)

        d = set(a)
        e = set(b)

        dict2 = {}
        if len(a) == len(b) and len(d) == len(e):
            for key, value in enumerate(b):
                dict2[value] = a[key]

            key2 = set()
            value2 = set()

            for k, v in dict2.items():
                key2.add(k)
                value2.add(v)

            if len(key2) == len(value2):
                return True
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    s =Solution()
    print(s.wordPattern("aba", "dog cat cat"))