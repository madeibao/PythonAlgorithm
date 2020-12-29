

# 一个矩阵，从左到右面和从上到下面都递增。



class Solution:
    def fine(self, target, array):
        if len(array) == 0 or len(array[0]) == 0:
            return False
        else:
            i = 0
            j = len(array[0])-1
            while i < len(array) and j >= 0:
                if array[i][j] < target:
                    i += 1
                elif array[i][j] > target:
                    j -= 1
                else:
                    return True
            # 默认的是返回没有的情况。
            return False




if __name__ == '__main__':

    matrix = [[1, 3, 15, 17, 19],
              [2, 4, 16, 17, 22],
              [3, 4, 21, 44, 51],
              [6, 7, 18, 29, 36]]
    a = 7
    ss = Solution()
    print(ss.fine(a, matrix))











