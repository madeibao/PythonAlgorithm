

def demo():
    ans = 0

    def inner():
        nonlocal ans
        ans += 1
        return ans
    inner()
    print(ans)

demo()


# nonlocal = 我要改外面那层函数里的变量，不是全局的，也不是我自己的。

