
class Solution:

    # array 二维列表

    def Find(self, target, array):

        # write code here

        for line in array:
            if target in line:
                return True
        return False


if __name__ == '__main__':
    target = 2
    array = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]

    solution = Solution()
    ans = solution.Find(target, array)
    print(ans)














