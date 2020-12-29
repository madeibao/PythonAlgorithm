
# 请实现一个函数，功能为合并两个升序数组为一个升序数组
# 点击页面左下角“例2”，了解如何实现输入输出
# 输入描述:
# 输入有多个测试用例，每个测试用例有1-2行，每行都是以英文逗号分隔从小到大排列的数字
# 输出描述:
# 输出一行以英文逗号分隔从小到大排列的数组
# 示例1
# 输入
# 复制
1,5,7,9
2,3,4,6,8,10

# # 输出的内容为：
# 1,2,3,4,5,6,7,8,9,10




def func(a, b):
    n, m = len(a), len(b)
    i, j = 0, 0
    res = []
    while i < n and j < m:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    if i < n:
        res += a[i:]
    if j < m:
        res += b[j:]
    res = map(str, res)
    print(','.join(res))


if __name__ == '__main__':
    try:
        line1 = list(map(int, input().strip().split(',')))
        line2 = list(map(int, input().strip().split(',')))
    except:
        line2 = []
    func(line1, line2)