

class Solution:
    def addStrings(self, a: str, b: str) -> str:    

        carry = 0

        res = ''
        i = len(a) - 1
        j = len(b) - 1

        while i>=0 or j>=0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            res += str(carry % 10)
            carry //= 10
        return "".join(reversed(res))


if __name__ == '__main__':
    stra = "123"
    strb = "234"

    print(Solution().addStrings(stra, strb))

