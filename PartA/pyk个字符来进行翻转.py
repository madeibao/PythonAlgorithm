




class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list2 = []
        for i in range(0, len(s), k):
            list2.append(s[i:i+k])
        list3 = []
        for i in range(0, len(list2)):
            if i % 2 == 0:
                list3.append(list2[i][::-1])
            else:
                list3.append(list2[i])

        return "".join(list3)


if __name__ == "__main__":
    s = Solution()
    str2="abcdefghijk"
    k =2
    print(s.reverseStr(str,k))

