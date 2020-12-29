给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：


	每组都有 X 张牌。
	组内所有的牌上都写着相同的整数。

仅当你可选的 X >= 2 时返回 true。
示例 1：

输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]



from functools import reduce
from collections import Counter
import math
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        values = Counter(deck).values()  # 首先建立了一个字典的关系内容。
        return reduce(math.gcd, values) >= 2   #


if __name__ == '__main__':
    s = Solution()
    print(s.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
















