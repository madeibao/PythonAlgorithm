



from typing import List

class Solution:
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
    s = Solution()
    pushed = [1,2,3,4,5]
    popped = [1,2,3,4,5]
    print(s.validateStackSequences(pushed, popped))

