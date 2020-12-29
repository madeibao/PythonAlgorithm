

5,70,[1,2,3,3,4]

2030

转换为一个最小堆的数来实现算法的更新和求解。



import heapq
class Solution:
    def solve(self , n , c , a ):
        # write code here
         
        total = 0
        heapq.heapify(a)
         
        while len(a) != 1:
            lc = heapq.heappop(a)
            rc = heapq.heappop(a)
            total += lc + rc
            heapq.heappush(a, lc+rc)
        return total*c


if __name__ == "__main__":
	s =Solution()
	n = int(input())
	c = int(input())
	list2 = list(map(int, input().split(" ")))
	print(s.solve(n,c,list2))

