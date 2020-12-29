# 给出字符串中的第一个唯一的字符。

class Solution():
    def firstUniqChar(self, s):
        length = len(s)
        for i in range(length):
            for j in range(length):
                if s[i] == s[j] and i != j:
                    break          # 提前中断可以提高效率
                elif j == length-1 :
                    return i
        return -1



class Solution():
    def firstUniqChar(self,s):
        length = len(s) 

        for i in range(length):
            for j in range(length):
                if s[i] == s[j] and i != j:
                    break
                elif j == length-1:
                    return i
        return -1

        

if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("loveleetcode"))



