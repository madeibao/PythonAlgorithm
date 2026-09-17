# 字符串的幂集合运算结果值。

class Solution:
    def stringPowerSet(self, strs: str) -> list:
        N = len(strs)
        res = []
        for i in range(2 ** N):
            temp = ""
            for j in range(N):
                if (i >> j) % 2:
                    temp += strs[j]  # 修复：取出对应位置字符
            res.append(temp)
        return res


if __name__ == "__main__":
    s = Solution()
    str2 = "abc"
    print(s.stringPowerSet(str2))
