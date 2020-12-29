

# python的增减字符串的匹配的操作。

# 输出："IDID"
# 输出：[0,4,1,3,2]

# 输出："III"
# 输出：[0,1,2,3]

# 输出："DDI"
# 输出：[3,2,0,1]




from typing import List


class Solution():
    def diStringMatch(self, S: str) -> List[int]:
        length = len(S)
        list2 = [i for i in range(length+1)]



        return list2


if __name__ == '__main__':
    s = Solution()
    print(s.diStringMatch("IDID"))






