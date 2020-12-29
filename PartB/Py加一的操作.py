# -*- coding: utf-8 -*-
[1, 2 ,3]
变成为
[1, 2, 4]


from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str2 =str()
        for i in digits:
            str2 += str(i)
        str3 = int(str2)
        str3+=1
        list3 =[]
        for i in str(str3):
            list3.append(int(i))
        return list3
            

if __name__ == "__main__":
    s = Solution()
    list2 = [1, 2, 3]
    print(s.plusOne(list2))

