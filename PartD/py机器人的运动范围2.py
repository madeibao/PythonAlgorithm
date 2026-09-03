

class Solution(object):
	def movingCount(self, m: int, n: int, k: int) -> int:
		visited = [[False for _ in range(n)] for _ in range(m)]
		return self.getvisited(0,0,m,n,visited, k)

	def getvisited(self, i, j, m, n, visited, k):
		if i<0 or i>=m or j<0 or j>=n or self.calc(i) + self.calc(j)>k or visited[i][j]==True:
			return 0
		visited[i][j] = True
		return self.getvisited(i-1, j, m, n, visited, k) + self.getvisited(i+1, j,m, n, visited, k) + self.getvisited(i,j-1,m, n, visited, k) + self.getvisited(i,j+1,m, n, visited, k)+1

	def calc(self, num):
		res = 0
		while num>0:
			res += num%10
			num //= 10
		return res

if __name__ == "__main__":
	s = Solution()
	m = 2
	n = 3
	k = 1
	print(s.movingCount(m, n, k))
	