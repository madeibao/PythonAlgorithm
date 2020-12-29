from typing import List

class Solution:
    def twoSum(self, n: int) -> List[float]:
        if n == 0:
            return []
        # 初始化 1 - 6 是 1次，7 - n 是 0 次。
        # 编号从1开始，这样方便写代码。  为了从1开始，我们只需要在数组前面随便push一个元素即可，比如本例的0
        cnts = [0] + [1] * 6 + [0] * (6 * n - 6)
        # 模拟投掷 n - 1 次
        for _ in range(n - 1):
            # 从后向前更新
            for i in range(6 * n, 0, -1):
                cnts[i] = sum(cnts[max(i - 6, 0): i])

        return list(filter(lambda a: a != 0, list(map(lambda a: a / 6 ** n, cnts))))


if __name__ == "__main__":
	s = Solution()
	print(s.twoSum(2))

