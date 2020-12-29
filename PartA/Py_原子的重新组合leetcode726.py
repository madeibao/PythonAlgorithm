'''
给定一个化学式formula（作为字符串），返回每种原子的数量。
原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。
如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。
两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。
一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。
给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），
然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。

示例 1:

输入: 
formula = "H2O"
输出: "H2O"
解释: 
原子的数量是 {'H': 2, 'O': 1}。


示例 2:

输入: 
formula = "Mg(OH)2"
输出: "H2MgO2"
解释: 
原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
'''
# 题目是有难度的。

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        from collections import defaultdict
        n = len(formula)
        i = 0
        lookup = defaultdict(int)
        stack = []    # 创建一个栈，用列表来模拟栈的结构。
        while i < n:
            if formula[i] == "(":
                stack.append(lookup.copy())
                lookup.clear()
                i += 1
            elif formula[i] == ")":
                right = i + 1
                val = 0
                while right < n and formula[right].isdigit():
                    val = val * 10 + int(formula[right])
                    right += 1
                if val == 0:
                    t_num = 1
                else:
                    t_num = val
                if stack:
                    tmp = lookup.copy()
                    lookup = stack.pop()
                    for k in tmp:
                        lookup[k] = lookup[k] + tmp[k] * t_num
                i = right
            else:
                right = i
                while right < n - 1 and formula[right + 1].islower():
                    right += 1
                tmp = formula[i:right + 1]
                i = right + 1

                val = 0
                while i < n and formula[i].isdigit():
                    val = val * 10 + int(formula[i])
                    i += 1
                if val == 0:
                    val = 1
                lookup[tmp] = lookup[tmp] + val


        res = ""
        for k in sorted((lookup.keys())):
            if lookup[k] != 1:
                res += k + str(lookup[k])
            else:
                res += k
        return res


cc = Solution()
print(cc.countOfAtoms("K4(ON(SO3)2)2"))