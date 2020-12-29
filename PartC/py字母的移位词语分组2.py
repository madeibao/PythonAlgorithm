
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapx = dict()
        for i in strs:
            tmp = ''.join(sorted(list(i)))
            if tmp in mapx.keys():
                # 字典的值为一个列表。
                mapx[tmp].append(i)
            else:
                mapx[tmp] = [i]
        return list(mapx.values())
        


if __name__=="__main__":
	s =Solution()
	strs =["eat", "tea", "tan", "ate", "nat", "bat"]
	print(s.groupAnagrams(strs))

