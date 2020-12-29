


# 给定两个数组，判断数组的一个是否为另一个的出栈的序列。
# 一共两个数组，其中一个入栈，一个出栈

#----------------------------------------------------------------

class Solution():
    def stackOrder(self, list2, list3):
        stack = []
        j = 0
        for i in range(len(list2)):
            stack.append(list2[i])
            while j < len(list3) and stack[-1] == list3[j]:
                stack.pop()
                j += 1
        return stack==[]


if __name__ == "__main__": 
    s2 = Solution()
    list2 = [1,2,3,4,5]
    list3 = [4,5,3,2,1]

    print(s2.stackOrder(list2 ,list3))

