
from typing import List


class Solution():
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        dict={'a':'2','b':'2','c':'2','d':'3','e':'3','f':'3','g':'4','h':'4','i':'4','j':'5','k':'5','l':'5',
        'm':'6','n':'6','o':'6','p':'7','q':'7','r':'7','s':'7','t':'8','u':'8','v':'8','w':'9','x':'9','y':'9','z':'9'}
        ans=[]
        for word in words:
            temp=''
            for char in word:
                temp+=dict[char]
            if temp==num:
                ans.append(word)
        return ans


if __name__ == "__main__":
    num = "8733"
    words = ["tree", "used"]

    s = Solution()
    print(s.getValidT9Words(num, words))





