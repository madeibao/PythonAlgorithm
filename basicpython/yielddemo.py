
def simple_gen():
    print("开始")
    yield 1
    print("继续")
    yield 2
    print("结束")

g = simple_gen()
print(next(g))
print(next(g))




# 迭代器，不会一次完整加载内存，而是分布计算

