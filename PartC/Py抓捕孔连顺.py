
# 字节跳动抓捕孔连顺



class Solution():
    def getNum(self,n,k,nums):
        idx = 0
        res = []

        for m in range(2,n):
            while idx<=m-2:
                if nums[m]-nums[idx]>d:
                    idx+=1
                else:
                    break
            res.append((m-idx)*(m-idx-1)//2)
        return sum(res)%99997867

if __name__ == '__main__':
    n, d = list(map(int, input().strip().split()))
    seq = list(map(int, input().strip().split()))
    s2 = Solution()
    print(s2.getNum(n,d,seq))



