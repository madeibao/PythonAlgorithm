
from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            for j in range((len(row) + 1) // 2):
                if row[j] == row[-1-j]:             # 采用Python化的符号索引
                    row[j] = row[-1-j] = 1 - row[j]    
        return A
                    
if __name__ == "__main__":
    s = Solution()  
    list2  =[[1,1,0],[1,0,1],[0,0,0]]
    print(s.flipAndInvertImage(list2))

