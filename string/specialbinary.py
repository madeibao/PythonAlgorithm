


class Solution:
    def checkOnesSegment(self, s: str) -> bool: 
        return not "01" in s
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkOnesSegment("1001"))