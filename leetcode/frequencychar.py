

class Solution:
    def frequencySort(self, s: str) -> str:
        
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

        res = ""
        for i in sorted_dict:
            res += i[0] * i[1]
        return res
    
if __name__ == '__main__':
    s = "tree"
    print(Solution().frequencySort(s))

