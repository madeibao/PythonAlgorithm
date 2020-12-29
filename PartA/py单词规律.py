

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        list2 = str.split(" ")

        if len(pattern)!=len(str):
            return False
        if len(set(pattern))!=len(set(list2))：
            return False

        if len(set(zip(pattern,list2)))=len(set(pattern)):
            return False
        else:
            return True



if __name__ == "__main__":
    s =Solution()
    pattern = "abba", str = "dog cat cat dog"
    print(s.wordPattern(pattern, str))

