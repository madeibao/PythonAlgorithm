

class Solution:
	def movingCount(self, m, n, k):

	    visited=[[False for _ in range(n)] for _ in range(m)] #定义标记访问状态
	    return self.DFS(0,0,m,n,visited,k) #初始状态是原点

	def DFS(self,i,j,m,n,visited,k):
		# 边界条件已经访问过，那么是什么情况。
	    if i<0 or i>=m or j<0 or j>=n or self.cal(i)+self.cal(j)>k or visited[i][j]==True: #边界条件
	        return 0
	    visited[i][j]=True
	    #回溯子状态
	    return self.DFS(i-1,j,m,n,visited,k)+self.DFS(i,j-1,m,n,visited,k)+self.DFS(i+1,j,m,n,visited,k)+self.DFS(i,j+1,m,n,visited,k)+1
	    
	def cal(self,num): #计算行坐标和列坐标数位和

	    total=0
	    while num>0:
	        total+=num%10
	        num//=10
	    return total

#---------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        self.visited = [[False for _ in range(n)] for _ in range(m)]
        self.process(m, n, 0, 0 ,k)
        return sum(sum(self.visited, []))
    
    def process(self, m, n, i, j, k):
        if i < 0 or i > m - 1 or j < 0 or j > n -1 or self.getSum(i, j) > k or self.visited[i][j]:
            return
        self.visited[i][j] = True
        self.process(m, n, i - 1, j, k)
        self.process(m, n, i + 1, j, k)
        self.process(m, n, i, j - 1, k)
        self.process(m, n, i, j + 1, k)

    def getSum(self, i, j):
        return sum(map(int, str(i)+str(j)))


if __name__ == "__main__":
	s = Solution()
	m = 2 
	n = 3
	k = 1

	print(s.movingCount(m, n, k))



