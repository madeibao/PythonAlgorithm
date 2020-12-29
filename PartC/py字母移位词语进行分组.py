
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
        

if __name__ == "__main__":
    s  =Solution()
    list2 =  ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(list2))


# ---------------------------------------------------------------------------------------
# 下面的语句把字典长度值是一个情况排除在外。

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
        
        res = []
        for k,v in mapx.items():
            if len(v) >1:
                res.append(v)
        return res

        

if __name__ == "__main__":
    s  =Solution()
    list2 =  ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(list2))



#////////////////////////////////////////////////////////////////////////////////////////////////
# 牛逼哄哄的写法。
# 

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
                
        list2 = list(mapx.values())

        #通过调用python的过滤器来实现更好的过滤掉，把分组长度为1的内容来过滤掉。
        # filter的第二个参数是一个可迭代的对象。
        newlist = list(filter(lambda x:len(x)>1,list2))
        return newlist
        

if __name__ == "__main__":
    s  =Solution()
    list2 =  ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(list2))



class Solution(object):
	def groupAnagrams(self, strs):

		dict2 = {}

		for i in strs:
			temp = list(sorted(i))

			if temp in dict2.keys():
				dict2[temp].append(i)
			else:
				dict2[temp] = i

		