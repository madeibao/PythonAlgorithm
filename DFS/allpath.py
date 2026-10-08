
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]
        def dfs(i,arr):
            if i==len(graph)-1:
                ans.append(arr)
            for j in graph[i]:
                dfs(j, arr+[j])
        dfs(0,[0])
        return ans

if __name__ == "__main__":
    graph = [[1,2],[3],[3],[]]
    solution = Solution()

    print(solution.allPathsSourceTarget(graph))
    # Output: [[0, 1, 3], [0, 2, 3]]

    