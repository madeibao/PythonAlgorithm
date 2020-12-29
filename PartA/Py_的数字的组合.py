

#C(m,n)=C(m-1,n)+C(m-1,n-1)
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 示例:
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k>n or k==0:
            return []
        if k==1:
            return [[i] for i in range(1,n+1)]
        if k==n:
            return [[i for i in range(1,n+1)]]
        
        answer=self.combine(n-1,k)
        for item in self.combine(n-1,k-1):
            item.append(n)
            answer.append(item)
        
        return answer


# 简单回溯法解决问题
class Solution(object):
    def combine(self, n, k):
        tmp, ret = [], []
        self.dfs(n, k, 1, tmp, ret)
        return ret

    def dfs(self, n, k, index, tmp, ret):
        if len(tmp) == k:
            ret.append(tmp[:])
            return
        for i in range(index, n + 1):
            tmp.append(i)
            self.dfs(n, k, i + 1, tmp, ret)
            tmp.pop()


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(start, k):
            if k == 0:
                res.append(path.copy())
            else:
                for i in range(start, n - k + 2):
                    path.append(i)
                    backtrack(i + 1, k - 1)
                    path.pop()
        backtrack(1, k)
        return res




cc=Solution()
print(cc.combine(4,2))

