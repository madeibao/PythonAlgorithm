


# 判断是否为合法的匹配括号。


class Solution():
    def validBracket(self, nums):
        dic2 = {"(":")","{":"}","[":"]"}

        stack = []
        for i in range(len(nums)):
            if nums[i] in dic2:
                stack.append(nums[i])
            elif len(stack)!=0 and dic2[stack[-1]]==nums[i]:
                stack.pop()
            else:
                return False
        return stack==[]

if __name__ == "__main__":
    s = Solution()
    str2 = "(){}"
    print(s.validBracket(str2))
