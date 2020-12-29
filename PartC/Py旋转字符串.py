

# 给定一个字符串
# 给出字符的旋转的结果值

#---------------------------------------------------------------------
A  ="abcde"
list1 = []

for i in range(len(A)):
	str2 = ""
	str2 += A[i + 1:] + A[:i + 1]
	list1.append(str2)

print(list1)
#--------------------------------------------------------------------     
# 最终的得到的结果为：

# ['bcdea', 'cdeab', 'deabc', 'eabcd', 'abcde']


# ------------------------------
# 网上给出的另一个比较新颖的解答方式。

# 给定的是一个字符串的值。
# 例如  abcde 经过字符串的旋转的操作可以变成  cdeab
# 试问 一个字符串能否经过旋转的操作来变成另一个字符串的值。


def isxuan(A, B):
    if B in A+A:
        return True
    else:
        return False


print(isxuan("abcde", "cdeab"))

