
class Solution:
    def crackNumber(self, ciphertext: int) -> int:
        res = []
        str_num = str(ciphertext)
        #  initialize the res array with 1s for the base cases
        res =[1 for i in range(len(str_num)+1)]
        n = len(str_num)
        
        for i in range(2, n+1):
            if str_num[i-2]=='1' or (str_num[i-2]=='2' and str_num[i-1] <= '6'):
                res[i] = res[i-1] + res[i-2]
            else:
                res[i] = res[i-1]
        return res[n]

if __name__ == "__main__":
    sol = Solution()
    ciphertext = 226
    print(sol.crackNumber(ciphertext))  # Output: 3

