


# 判断是否为栈的输入和输出序列。
class Solution(object):
    def stackorder(self,inOrder, outOrder):
        i, j = 0, 0

        stack = []
        while i<len(inOrder) and j<len(outOrder):
            stack.append(inOrder[i])
            while stack and stack[-1]==outOrder[j]:
                stack.pop() 
                j+=1
            i+=1
        return stack==[]


if __name__ == "__main__":
    s  = Solution()
    inOrder = [1,2,3,4,5]
    outOrder = [5,4,3,2,1]

