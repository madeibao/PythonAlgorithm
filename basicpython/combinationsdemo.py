

from itertools import combinations
from itertools import permutations


# 从列表 [1, 2, 3] 中取 2 个元素的所有组合
result = list(combinations([1, 2, 3], 2))


result2 = list(permutations([1, 2, 3], 2))


if __name__ == "__main__":
    print(result)
    # 输出: [(1, 2), (1, 3), (2, 3)]
    print(result2)
    # 输出: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


