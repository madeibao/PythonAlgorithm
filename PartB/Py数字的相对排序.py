


from typing import List

class Solution():
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        not_exist = []
        exist = []
        s = set(arr2)
        ans = []
        for a in arr1:
            if a in s:
                exist.append(a)
            else:
                not_exist.append(a)
        cnt = collections.Counter(exist)
        for a in arr2:
            ans += [a] * cnt[a]
        return ans+sorted(not_exist)

if __name__ == "__main__":
    s = Solution()
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]

    print(s.relativeSortArray(arr1, arr2))

