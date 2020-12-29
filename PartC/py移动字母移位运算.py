

 
# 关键是前缀的数组要想到，其实都能想到。
from typing import List
 
 
class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        temp = []
 
        for i in range(len(shifts)):
            temp.append(sum(shifts[i:]))
 
        res = []
        for i in range(len(shifts)):
            res.append(chr((ord(S[i]) + temp[i] - 97)%26 + 97))
        return "".join(res)
 
 
if __name__ == "__main__":
    s = Solution()
    str2 = "abc"
    shifts = [3,5,9]
    print(s.shiftingLetters(str2, shifts))

    