def legal(strs):
    dict2 = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for char in strs:
        # 如果是左括号，压栈
        if char in dict2:
            stack.append(char)
        else:
            # 是右括号：栈空直接失败；栈顶对应右括号不等于当前字符则失败
            if not stack or dict2[stack[-1]] != char:
                return False
            stack.pop()
    # 全部遍历完，栈必须为空才算全部匹配
    return len(stack) == 0


class Solution:
    pass


if __name__ == '__main__':
    s = Solution()
    str2 = "()()"
    print(legal(str2))  # True
    print(legal("(]"))  # False
    print(legal("((("))  # False
    print(legal("{[]}"))  # True
