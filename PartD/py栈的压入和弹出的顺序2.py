

class Solution(object):
    def stackOrder(self,pushed, popped):
        
        j = 0
        stack = [] #
        for x in pushed:
            stack.append(x)
            if len(stack)>0 and stack[-1] == popped[j]:
                j+=1
                stack.pop()
        # return stack==[] 
        return not stack


if __name__ == "__main__":
    s = Solution()
    list2 = [1,2,3,4,5]
    list3 = [1,2,3,4,5]
    print(s.stackOrder(list2,list3))



