

# # 字母的大小的排列内容。
# # 字母的排列。
# import string
# from typing import List
# class Solution():
#     def letterCasePermutation(self, S: str) -> List[str]:
#         if not S:
#             return []
#         # 从字符串数组中来添加内容。
#         res = ['']
#         for i in  S:
#             temp = []
#             for j in res:
#                 if i in string.ascii_letters:
#                     temp.append(j+i.lower())
#                     temp.append(j+i.upper())
#                 else:
#                     temp.append(j+i)
#             res = temp
#         return res


import string
from typing import List
class Solution():
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return []
        res = ['']

        for i in S:
            temp = []
            for j in res:
                if i in string.ascii_letters:
                    temp.append(j+i.lower())
                    temp.append(j+i.upper())
                else:
                    temp.append(j+i)
            res = temp
        return res
    
if __name__ == '__main__': 
    s =Solution()
    print(s.letterCasePermutation("ab12"))





