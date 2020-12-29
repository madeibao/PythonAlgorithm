

# 只需要交换字符串中的字符一次的结果就行。
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        # 如果式两个字符串相等的话，并且由重复的字符串来组成。
        if A == B and len(set(A)) < len(A):
            return True 

        # 保存结果值。
        l = []
        for i,j in zip(A,B):
            if i!=j:
                l.append((i,j))
        # 交换一次，所以最终只有两个元组内容是不同的。
        return len(l) == 2 and l[0] == l[1][::-1]


if __name__ == "__main__": 
	s = Solution()
	A = "ab"
	B = "ba"
	print(s.buddyStrings(A,B))



