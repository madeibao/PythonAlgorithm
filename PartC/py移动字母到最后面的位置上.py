

class Solution:
    def change(self , s ):
        # write code here
        num = s.count('a')
        res = "".join(list(filter(lambda x:x!='a', s)))
        res+=num*'a'
        return res


if __name__ == "__main__":
    s = Solution()
    str2 = "abcavv"
    print(s.change((str2)))