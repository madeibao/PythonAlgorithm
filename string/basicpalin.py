

# num = 5
# print(f'{num:08b}')  # 00000101

# num = 5
# binary = bin(num)[2:].zfill(8)  # bin(5) = '0b101'，[2:]去掉'0b'
# print(binary)  # 00000101


class Solution:
    def isPalindromic(self, s: str) -> bool:
        bits = "".join(f'{ord(c):08b}' for c in s)
        return bits == bits[::-1]

if __name__ == "__main__":
    s = "racecar"
    solution = Solution()
    result = solution.isPalindromic(s)
    print(result)  # Output: True
