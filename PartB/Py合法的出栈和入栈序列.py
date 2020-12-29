
from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack =[]
        # 列表来当作栈进行使用。
        i,j = 0,0
        while i < len(pushed) and j < len(pushed):
            stack.append(pushed[i])
            while stack and stack[-1]==popped[j]:
                stack.pop()
                j+=1
            i+=1

        return stack==[]


if __name__ == "__main__":
    s = Solution()
    list2 = [1,2,3,4,5]
    list3 = [4,5,3,2,1]

    print(s.validateStackSequences(list2,list3))

