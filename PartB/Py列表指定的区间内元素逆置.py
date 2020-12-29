


class Solution():
    def listReverse(self, list2, i, j):
        list2[i], list2[j] = list2[j], list2[i]
        i += 1
        j -= 1
        return list2


if __name__ == '__main__':
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    s = Solution()
    list3 = s.listReverse(list2, 2, 5)
    print(list3)



# [1, 2, 6, 4, 5, 3, 7, 8, 9, 10]