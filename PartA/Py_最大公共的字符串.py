def LCS_str(s1, s2):
    # 求2个字符串的最大公共字符串

    # 求对角线上的

    arr = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]

    max1 = 0

    p = 0

    for i in range(len(s1)):

        for j in range(len(s2)):

            if s1[i] == s2[j]:

                arr[i][j] = arr[i - 1][j - 1] + 1
                if arr[i][j] > max1:
                    max1 = arr[i][j]

                    p = i + 1

    return s1[p - max1:p]


a = input()
b = input()
print(LCS_str(a, b))



# 例如输入：asdf
#          asdf22

# 返回的是 asdf




