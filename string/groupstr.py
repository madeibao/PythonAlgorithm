



class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        dict = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key not in dict:
                dict[key] = []
            dict[key].append(s)

        return list(dict.values())

if __name__=="__main__":
    lists = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(lists))

    lists = [""]
    print(Solution().groupAnagrams(lists))

    lists = ["a"]
    print(Solution().groupAnagrams(lists))

    