


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         self.res = []
#         def dfs(route, left, right):
#             if left == 0 and right == 0:
#                 self.res.append(route)
#                 return
#             if left > right:
#                 return
#             if left < 0 or right < 0:
#                 return
#             dfs(route + '(', left - 1, right)
#             dfs(route + ')', left, right - 1)
#         dfs('', n, n)
#         return self.res

# if __name__ == '__main__':
# 	s = Solution()
# 	n2 = 3
# 	print(s.generateParenthesis(n2))




class Solution(object):
    def generage(self, n):
        self.res = []

        def fun2(strs, left, right):

            if left == 0 and right == 0:
                self.res.append(strs)
                return
            if left > right:
                return
            if left < 0 or right < 0:
                return

            fun2(strs + '(', left - 1, right)
            fun2(strs + ')', left, right - 1)
        fun2(str(), n, n)
        return self.res


if __name__ == '__main__':
    s = Solution()
    n = 3
    print(s.generage(n))

