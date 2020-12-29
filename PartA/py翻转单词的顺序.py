

class Solution(object):
    def reverse(self,strs):
        strs =strs.strip()
        list2 = strs.split()
        return " ".join(list2[::-1])

if __name__ == "__main__":
    s = Solution()
    str2 = "the sky is blue"
    print(s.reverse(str2))

