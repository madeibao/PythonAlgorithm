from typing import List
from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        返回数组中第 k 大的元素（使用大小为 k 的小顶堆维护前 k 大元素）

        Args:
            nums: 待查找的整数数组
            k: 目标排名（从大到小），取值范围为 1 到 len(nums)

        Returns:
            数组中第 k 大的元素
        """
        heap = []  # 小顶堆，堆顶为当前前 k 大元素中的最小值
        for num in nums:
            if len(heap) < k:
                heappush(heap, num)  # 堆未满，直接入堆
            else:
                if num > heap[0]:  # 比堆顶大，说明能挤入前 k 大
                    heappop(heap)  # 弹出当前最小元素
                    heappush(heap, num)  # 新元素入堆

        return heap[0]  # 堆顶即为第 k 大元素

if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(Solution().findKthLargest(nums, k))  # 应输出 5

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(Solution().findKthLargest(nums, k))  # 应输出 4

