

def main():
    s = input("input a string:")
    ls = s.split(" ")
    print(len(ls))


if __name__ == '__main__':
    main()



"""
这里统计得出一共有100维度的向量.
词向量的大小为100维度.
对于这种有空格的文本,实际是按照文本的格式进行存储,按照字符串进行测试.
同样的是两个数据之间的空格可能是一个回车或者是更大的空格,也同样的适用.


"""