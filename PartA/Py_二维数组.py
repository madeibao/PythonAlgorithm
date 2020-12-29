matrix = [[0 for i in range(5)] for i in range(5)]

print(matrix)

# 这里展示的是用python定义一个二维度的数组。


arr = input("")    # 输入一个一维数组，每个数之间使空格隔开
num = [int(n) for n in arr.split()]    # 将输入每个数以空格键隔开做成数组
print(num)


#===========================================


二维数组的遍历效果
list2 = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
for key, value in list2:
    print(key)
    print(value)


遍历的效果如下所示

1
0
-3
1
-4
0
2
3


二维数组的遍历的效果2


list2 = [[1,2,3],[4,5,6],[7,8,9]]

for i in list2:
	for j in i:
		print(j,end=' ')
	print("\n")

# 1 2 3
# 4 5 6
# 7 8 9


二维数据的行与列。


matrix = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2],
]


print(len(matrix))   		 # 代表行数
print(len(matrix[0]))       # 代表列数