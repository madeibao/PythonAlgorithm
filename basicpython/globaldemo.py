


a = 0  # 建议先在模块级定义，更清晰

def demo():
    global a
    a = 1          # 赋值单独一行

    def inner():
        global a   # inner 里也要声明，否则 a += 1 会报 UnboundLocalError
        for i in range(10):
            a += 1
    inner()


if __name__ == '__main__':
    demo()
    print(a)  # 输出 11，不是 10！