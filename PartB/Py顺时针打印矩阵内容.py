题目描述
给定一个数字矩阵，请设计一个算法从左上角开始顺时针打印矩阵元素
输入描述:
输入第一行是两个数字，分别代表行数M和列数N；接下来是M行，每行N个数字，表示这个矩阵的所有元素；当读到M=-1，N=-1时，输入终止。
输出描述:
请按逗号分割顺时针打印矩阵元素（注意最后一个元素末尾不要有逗号！例如输出“1，2，3”，而不是“1，2，3，”），每个矩阵输出完成后记得换行


3 3
1 2 3
4 5 6
7 8 9
-1 -1



def clock_print(matrix):
    c = []
    while True:
        try:
            c.extend(matrix.pop(0))
            for i in range(len(matrix) - 1):
                c.append(matrix[i].pop())
            c.extend(matrix.pop(-1)[::-1])
            for i in range(-len(matrix) + 1, 0):
                c.append(matrix[-i].pop(0))
        except IndexError:
            break
    return c


while True:
    M, N = [int(i) for i in input().split()]
    if M == -1 and N == -1:
        break
    matrix = [[str(i) for i in input().split()] for m in range(M)]
    result = clock_print(matrix)
    print(','.join(result))