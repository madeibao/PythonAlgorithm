

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False for i in range(len(s)+1)]
        dp[0]=True

        for i in range(len(s)):
            if dp[i]==True:
                for j in range(i+1,len(s)+1):
                    if s[i:j] in wordDict:
                        dp[j]=True
        # 返回是否能够有效的进行拆分
        
        # 返回最后的一个值是否为真。
        return dp[-1]

if __name__ == "__main__":
	s =Solution()
	s2 "leetcode"
	list2 = ['leet','code']
	print(s.wordBreak(s2,list2))

	








