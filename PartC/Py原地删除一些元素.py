



class Solution():
    def keeyone(self, A, num):
        length = len(A)
        idx = 0
        for i in range(length):
            if A[i] != num:
                A[idx] = A[i]
                idx += 1
        return idx


if __name__ == "__main__":
    print(Solution().keeyone([1, 2, 2, 3], 3))





# 给定一个列表和是一个元素，然后删除列表中与元素相等的内容。
# 最后返回的是删除后的元素的长度值。




