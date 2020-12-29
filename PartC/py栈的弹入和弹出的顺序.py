


class Solution(object):
    def order2(self,headA, headB):
        stack = []  
        j = 0
        for x in headA:
            stack.append(x)
            while stack and j<len(headB) and stack[-1]==headB[j]:
                j+=1
                stack.pop()
        return stack==[] 

if __name__ == "__main__":
    s = Solution()
    pushed = [1,2,3,4,5]
    popped = [1,2,3,4,5]
    print(s.order2(pushed,popped))

    