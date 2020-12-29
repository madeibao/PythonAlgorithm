class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        if num == 1:
            return True
        if num % 2 == 0:
            num = num // 2
        elif num % 3 == 0:
            num = num // 3
        elif num % 5 == 0:
            num = num // 5
        else:
            return False
        return self.isUgly(num)
        






if __name__ == "__main__":
    s= Solution()
    print(s.isUgly(6))