

from typing import List
from typing import Tuple

class Solution():
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return not stack

if __name__ == "__main__":
    list2 = [1, 2 ,3 ,4 , 5]
    list3 =  [4,5,3,2,1]
    s = Solution()
    print(s.validateStackSequences(list2,list3))

    