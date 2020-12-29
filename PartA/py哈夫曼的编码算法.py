'''
题意：
牛牛现在在学习计算机，他想通过计算机计算n个数的和。
但是计算机计算数字的和是有花费的，比如计算x，y两个数的和，需要花费(c*x+c*y)(c∗x+c∗y)秒。
计算机一次只能计算一次，牛牛想知道自己怎么合理安排计算的顺序，可以使得花费的时间最短。

输入：
给定n,c。
给定a数组，ai表示第i个数的大小。

(1 \leq n\leq 2*10^{5}1≤n≤2∗10 
5
  , 1 \leq c\leq 1001≤c≤100 )
(1 \leq a_{i} \leq 10^{2}1≤a 
i
​	
 ≤10 
2
 )

输出：
一个数字表示输出计算n个数字和的最小花费的时间。
示例1
输入
复制
5,76,[81,30,76,24,84]
输出
复制
48944
'''


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
	s = Solution()
	n, c = map(int, input().split(" "))
	list2 = list(map(int, input().split(" ")))
	print(s.solve(n, c, list2))