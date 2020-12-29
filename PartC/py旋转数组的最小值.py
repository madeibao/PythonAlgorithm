




# 通过二分法的方式来了解旋数组的最小值。


class Solution:
    def minArray(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]: i = m + 1
            elif numbers[m] < numbers[j]: j = m
            else: j -= 1
        return numbers[i]


if __name__ == "__main__":
	s = Solution()
	list2 = [3,4,5,1,2]
	print(s.minArray(list2))

