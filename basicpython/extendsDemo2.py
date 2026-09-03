


class A:
    def greet(self):
        return "Hello from A"

class B(A):
    pass

class C(A):
    def greet(self):
        return "Hello from C"

class D(B, C):
    pass

if __name__ == '__main__':

    print(D().greet())
    print(D.__mro__)

# D 无 greet → B 无 greet → **找到 C 的 greet，直接执行**，不再走到 A