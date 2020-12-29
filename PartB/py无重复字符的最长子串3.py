


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
   
        maxLength = 0
        for i, _ in enumerate(s):    # 这里没有使用range函数
            count = 0
            usedChar = str()
            for j in s[i:]:
                if j not in usedChar:
                    usedChar += j
                    count += 1
                    if maxLength < count:  # 这里没有使用max函数
                        maxLength = count
                else:
                    break
        return maxLength


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
   
        maxLength = 0
        for i, _ in enumerate(s):    # 这里没有使用range函数
            count = 0
            usedChar = str()
            for j in s[i:]:
                if j not in usedChar:
                    usedChar += j
                    count += 1
                    if maxLength < count:  # 这里没有使用max函数
                        maxLength = count
                else:
                    break
        return maxLength
#-----------------------------------------------------------------------    ------------------------------------------

class Solution:
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        res = []
        for i in s:
            while i in res:
                res.pop(0)
            res.append(i)
            max_length = max(max_length, len(res))
        return max_length


if __name__ == "__main__":
    s = Solution()
    str2 = "abcdefghijklmnopqrstuvwxyzz"
    print(s.lengthOfLongestSubstring(str2))




