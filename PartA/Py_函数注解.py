




# Python 3 extends the feature by allowing you to attach metadata to functions describing their parameters and return values.
# 简单的说-> 就是为了告诉用户 具体参数和参数的类型。


def sum(x: int, y: int) -> int:  # python语言的新特性。
    return x+y

print(sum(2, 3))



class Spam:
    def bar(self, x: int, y: int):
        print('Bar 1:', x, y)

    def bar(self, s: str, n: int = 0):
        print('Bar 2:', s, n)


s = Spam()
print(s.bar(2, 3))     
print(s.bar('hello'))  


Bar 2: 2 3
None
Bar 2: hello 0
None










