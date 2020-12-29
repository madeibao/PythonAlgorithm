

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for tmp in zip(*strs):
            if len(set(tmp)) == 1:
                result += tmp[0]
            else:
                break
        return result


if __name__ == "__main__":
    s = Solution()
    str2 = ["flower", "flow", "flight"]

    print(s.longestCommonPrefix(str2))




class Solution(object):
    def longestCommonPrefix(self,strs):
        res = ""

        for temp in zip(*strs):
            if len(set(temp))==1:
                res += temp[0]
            else:
                break
        return res 


if __name__ == "__main__":
    s = Solution()
    
