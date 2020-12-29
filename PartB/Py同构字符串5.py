

# 判断两个字符串是否为同构的字符串。
class Solution():
    def sameStucture(self,s, t):
        if len(s) != len(t):
            return False

        if(len(set(s)) != len(set(t))):
            return False

        if(len(set(zip(s,t))) != len(set(t))):
            return False
        else:
            return True


if __name__ == "__main__":

    s = Solution()
    s2 = "abb"
    s3 = "cdd"
    print(s.sameStucture(s2, s3))

