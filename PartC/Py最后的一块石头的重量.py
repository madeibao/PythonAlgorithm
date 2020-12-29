
from typing import List


class Solution():
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) >= 2:
            a = stones[0]
            b = stones[1]
            if a == b:
                stones.remove(a)
                stones.remove(b)
                stones.sort(reverse=True)
            if a != b:
                stones.remove(a)
                stones.remove(b)
                stones.append(abs(a - b))
                stones.sort(reverse=True)
        while len(stones) == 0:
            return 0
        while len(stones) == 1:
            return stones[0]


if __name__ == "__main__":
    nums = [2, 7, 4, 1, 8, 1]
    s = Solution()
    print(s.lastStoneWeight(nums))




# ---------------------------------------------------------------
#----------------------------------------------------------------
# 方法2的内容
# 使用大顶堆。

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>=2:
            stones.sort()
            stones.append(stones.pop()-stones.pop())
        return stones[0]


#=========================================================================================================
#=========================================================================================================
#============================================================================

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq  ## heapq库是专门处理最小堆的库
        stones_heap = [-i for i in stones]  ## 用取负数的办法弯道处理最大堆问题
        heapq.heapify(stones_heap)  ## 把list最小推结构化；时间复杂度是O(n)
        while len(stones_heap) > 1:  ## 当至少还有2块石头的时候
            a = heapq.heappop(stones_heap)  ## 取出质量最大的石头（因为是负数，所以值是最小）；时间复杂度是O(logn)，因为取出后还要用logn的时间保持堆结构
            b = heapq.heappop(stones_heap)  ## 在剩下的石头里取出质量最大的石头；时间复杂度是O(logn)
            if a < b:  ## 如果第一块石头比第二块重，那么把摩擦剩下的小石头放进堆里
                heapq.heappush(stones_heap, a - b)  ## 如果两块石头一样重，就都没有了
        if stones_heap:
            res = -stones_heap[0]  ## 如果剩下石头，那么返回值是其质量
        else:
            res =  0  ## 如果不剩下石头，那么返回值是0
        return res



