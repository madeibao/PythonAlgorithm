
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    a = "11"
    b = "1"
    solution = Solution()
    result = solution.addBinary(a, b)
    print(result)  # Output: "100"


