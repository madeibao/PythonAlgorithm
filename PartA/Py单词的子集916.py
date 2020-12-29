

import collections

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ## 统计最大字母频率 ，然后比较.
        res = []
        dict_list = [collections.Counter(i) for i in B]
        max_dict = {}
        for i in dict_list :
            for k,v in i.items() :
                max_dict[k] = max(max_dict.get(k,0),v)
        #print(max_dict)
        for a in A :
            a_count = collections.Counter(a) 
            for k,v in max_dict.items() :
                if v > a_count.get(k,0) :
                    break
            else :
                res.append(a)
        return res


if __name__ == "__main__":
	s = Solution()
	A = ["amazon","apple","facebook","google","leetcode"]
	B = ["e","o"]

	print(s.wordSubsets(A,B))

# ----------------------------------------------------------------------------------------------------------------------
# =================================================================================================

class  Solution(object):
	def wordSubsets(self, A, B):
		res = []

		dict_list = [collections.Counter(i) for i in B]

		max_dict = dict()

		for i in dict_list:
			for k,v in i.items():
				max_dict[k]  = max(max_dict.get(k,0),v)

		for a  in A:
			aCounters = collections.Counter(a)
			for k,v in max_dict.items():
				if v>aCounters.get(k,0):
					break
				else:
					res.append(a)
		return res 

