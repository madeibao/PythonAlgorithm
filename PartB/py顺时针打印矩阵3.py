
class Solution(object):
    def spriral(self,nums):

        l = 0
        r = len(nums[0])-1

        t = 0
        b = len(nums)-1

        res = []
        while True:
            for i in range(l, r+1):
                res.append(nums[t][i])
            t+=1
            if t>b:break

            # 从上到下面遍历。
            for i in range(t, b+1):
                res.append(nums[i][r])
            r-=1
            if l>r:break

            # 从右到左
            for i in range(r, l-1,-1):
                res.append(nums[b][i])
            b-=1
            if t>b:break
            
            # 从下到上
            for i in range(b, t-1,-1):
                res.append(nums[i][l])
            l+=1
            if l>r:break

        return res


if __name__ == "__main__":
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.spriral(matrix))




