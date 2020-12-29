class Solution(object):
    def sortArrayByParity(self, A):
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])



if __name__ == "__main__":
    s  = Solution()
    print(s.sortArrayByParity([1,4,3,2,]))

