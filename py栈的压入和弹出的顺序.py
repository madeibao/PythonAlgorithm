

# 判断是否为合理的压入和弹出的顺序。

class Solution(object):
    def stackOrder(self,pushed, popped):

        stack= []
        j = 0
        for i in pushed:
            stack.append(i)
            if len(stack)>0 and j<len(poped) and stack[-1] == popped[j]:
                stack.pop()
                j+=1
        return stack==[] 


if  __name__ == "__main__": 
    s = Solution()
    pushed = [1,2,3,4,5]
    popped = [1,2,3,4,5]
    print(s.stackOrder(pushed,popped))



