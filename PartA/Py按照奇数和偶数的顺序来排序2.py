class Solution():
    def sortNumbers(self, nums):
        return [i for i in nums if i%2==0 ] + [j for j in nums if j%2==1 ]


if __name__ == "__main__":
    s = Solution()
    print(s.sortNumbers([2,3,1,4]))






