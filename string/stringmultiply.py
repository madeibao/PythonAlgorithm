
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        lena = len(num1) - 1
        lenb = len(num2) - 1

        res = [0] * (lena + lenb + 2)
        for i in range(lena, -1, -1):
            for j in range(lenb, -1, -1):
                # a = ord(num1[i]) - ord('0')
                # b = ord(num2[j]) - ord('0')
                a  = int(num1[i])
                b  = int(num2[j])
                mul = a * b
                sum_ = mul + res[i + j + 1]
                res[i + j] += sum_ // 10
                res[i + j + 1] = sum_ % 10
        
        while len(res)>1 and res[0]==0:
            res.pop(0)
        return ''.join(map(str, res))

if __name__ == "__main__":
    solution = Solution()
    num1 = "2"
    num2 = "3"
    print(solution.multiply(num1, num2))