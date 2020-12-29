

# 输出第n行中的第一个偶数的出现的位置，否则输出-1


from typing import List


class Solution():
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex):
            res.append([1])
            for j in range(1, i + 1):
                if j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i - 1][j - 1] + res[i - 1][j])
        return res


while True:
    try:
        if __name__ == '__main__':
            s = Solution()
            n = int(input())
            print(s.getRow(n))

    except:
        break
