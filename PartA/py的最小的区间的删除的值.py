


class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        n = len(array)
        maxx, minn = -float('inf'), float('inf')
        l, r = -1, -1
        for i in range(n):
            if array[i] < maxx: r = i
            else: maxx = array[i]
        for i in range(n-1, -1, -1):
            if array[i] > minn: l = i
            else: minn = array[i]

        return [l, r]

if __name__ == "__main__":
    s =Solution()
    list2 =[1,2,4,7,10,11,7,12,6,7,16,18,19]
    print(s.subSort(list2))

