
# 判断两个数字的结果值能否通过栈的压入和弹出来进行。

class Solution():
    def stackOrder(self,nums2, nums3):
        stack = []
        j = 0
        for x in nums2:
            stack.append(x)
            while stack and j<len(nums3) and stack[-1]==nums3[j]:
                j+=1
                stack.pop()
        return stack==[]


if __name__ == "__main__": 
    s =Solution()
    list2 = [1,2,3,4,5]
    list3 = [4,5,3,2,1]

    print(s.stackOrder(list2, list3))


