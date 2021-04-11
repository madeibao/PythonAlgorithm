


from typing import List 

class Solution:
    def permutation(self, s: str) -> List[str]:

        if not s:return None
        list2 = list(s)

        res = []
        def helper(start):
            if start==len(list2):
                res.append("".join(list2))
            for i in range(start, len(list2)):
                list2[i],list2[start] = list2[start],list2[i]
                helper(start+1)
                list2[i],list2[start] = list2[start],list2[i]
        helper(0)
        return res


if __name__ == '__main__':  
    s = Solution()
    str2 ="abc"
    print(s.permutation(str2))


