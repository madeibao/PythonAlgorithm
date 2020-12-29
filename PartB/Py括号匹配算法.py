

class Solution:
    def isValid(self, s: str) -> bool:
        li = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                li.append(i)
            if i == ')' or i == ']' or i == '}':
                if li == []:
                    return False
                elif abs(ord(i) - ord(li.pop(-1))) > 2:
                    return False
        return li == []


class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1
