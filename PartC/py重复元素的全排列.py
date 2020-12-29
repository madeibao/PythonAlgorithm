

class Solution(object):
    def fun2(self, nums):

        def helper(nums, size, depth, path, visited, res):

            if depth == size:
                res.append(path.copy())
            for i in range(len(nums)):
                if not visited[i]:
                    if i > 0 and nums[i - 1] == nums[i] and not visited[i - 1]:
                        continue

                    visited[i] = True
                    path.append(nums[i])
                    helper(nums, size, depth + 1, path, visited, res)

                    visited[i] = False
                    path.pop()

        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return nums

        res = []
        visited = [False for _ in range(n)]

        helper(nums, n, 0, [], visited, res)

        return res


if __name__ == "__main__":
    s = Solution()
    list2 = [1, 2, 2]
    print(s.fun2(list2))

