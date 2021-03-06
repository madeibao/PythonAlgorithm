

class Solution(object):
    def permutation(self,strs):
        res = []
        if not strs:
            return res  
        
        list2 = list(strs)
        def helper(i,list2, res):
            if i==len(list2):
                res.append("".join(list2))

            for k in range(i, len(list2)):
                list2[k],list2[i] = list2[i],list2[k]
                helper(i+1, list2, res)
                list2[k],list2[i] = list2[i],list2[k]
        
        helper(0, list2, res)
        return res


if __name__ == "__main__":
    s = Solution()
    str2 ="abc"
    res = s.permutation(str2)
    print(res)


#================================================================================================
# 去除字符串中大写字母后的全排列。
class Solution(object):
    def permutation(self, strs):
        res = []
        if not strs:
            return res
        list2 = list(strs)
        def helper(i, list2, res):
            if i == len(list2):
                res.append("".join(list2))
            for k in range(i, len(list2)):
                list2[k], list2[i] = list2[i], list2[k]
                helper(i + 1, list2, res)
                list2[k], list2[i] = list2[i], list2[k]
        helper(0, list2, res)
        return res

if __name__ == "__main__":
    s = Solution()
    str2 = input()
    s2 = ''.join(ch for ch in str2 if not ch.isupper())
    res = s.permutation(s2)
    print(res)

