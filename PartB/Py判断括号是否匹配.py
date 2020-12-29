
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dicts = {'(': ')', '{': '}', '[': ']'}  # 建立一个字典的形式
        stack = []
        lists = list(s)
        for item in lists:
            if item in dicts.keys():
                stack.append(item)
            elif item in dicts.values():
                if len(stack) == 0 or dicts.get(stack[-1]) != item:
                    return False
                else:
                    stack.pop()

        if len(stack) == 0:  # 所有的内容都匹配完璧，则为合法的表示形式。
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("((){}[])"))














