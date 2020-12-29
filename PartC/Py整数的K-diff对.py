

# 给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j), 其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k.

# 示例 1:

# 输入: [3, 1, 4, 1, 5], k = 2
# 输出: 2
# 解释: 数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
# 尽管数组中有两个1，但我们只应返回不同的数对的数量。



from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # 这里有一个细节需要注意的是: (1,3)等同于(3,1)
        # 所以我们无需将1,3都存储起来, 只要存储3即可. 因为k是确定的, 导致1也是确定的
        if k < 0:
            return 0
        # s存储遍历的元素, r存储上面注释的3
        s, r = set(), set()
        for n in nums:
            if n + k in s:
                r.add(n + k)
            if n - k in s:
                r.add(n)
            s.add(n)
        return len(r)


if __name__ == '__main__':
    s = Solution()
    print(s.findPairs([3, 1, 4, 1, 5], 2))
