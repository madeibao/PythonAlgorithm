# 1331. 数组序号转换

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hashmap={}
        L=sorted(list(set(arr)))
        for i,element in enumerate(L):
            hashmap[element]=i+1
        return [hashmap[i] for i in arr]
        

if __name__ == "__main__":
	s = Solution()
	list2 = [37,12,28,9,100,56,80,5,12]
	print(s.arrayRankTransform(list2))



