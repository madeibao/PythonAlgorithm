class Solution:
    def sortString(self, s: str) -> str:
        str_counter = collections.Counter(s)
        print(str_counter)
        result = []
        flag = False
        while str_counter:
            keys = list(str_counter.keys())
            keys.sort(reverse=flag)
            flag = not flag
            result.append(''.join(keys))
            str_counter -= collections.Counter(keys)
        return ''.join(result)


