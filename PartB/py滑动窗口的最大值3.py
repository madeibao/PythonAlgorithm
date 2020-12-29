

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res = []
        for i, num in enumerate(nums):
            while deque and deque[0] <= i - k: deque.popleft() # outdate indices
            while deque and num > nums[deque[-1]]: deque.pop()
            deque.append(i)
            if i >= k - 1:
                res.append(nums[deque[0]])
        return res

#----------------------------------------------------------------
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        n = len(nums)

        # 保存最终的结果值
        res = [0] * (n - k + 1)
        # i 表示下标的值。
        for i in range(len(nums)):
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
            idx = i - k + 1
            if idx >= 0:
                res[idx] = nums[deq[0]]
                # 弹出左面的元素值。
                if deq[0] == idx:
                    deq.popleft()
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(s.maxSlidingWindow(nums,k))

