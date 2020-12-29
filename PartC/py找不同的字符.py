


import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list((collections.Counter(t)-collections.Counter(s)).elements())[0]

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))



if  __name__ == "__main__": 
    str2= "abcd"
    str3="abcde"
    print(s.findTheDifference(str2, str3))
