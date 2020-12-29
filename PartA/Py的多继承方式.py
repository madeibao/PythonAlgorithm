


class A():
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
         print("B")

class C(A):
    def __init__(self):
        print("C")

class D(B,C):
    def __init__(self):
        print("D")


# ---------------------------------------------------------------------------------------------------------------------------
class A():
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")

class C(A):
    def __init__(self):
        print("C")

class D(B,C):
    pass
    # def __init__(self):
    #     print("D")

D()   # D里面没有，则找父类（从左往右），找到B
# B


#----------------------------------------------------------------------------------------------------------------------------

class A():
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
         print("B")

class C(A):
    def __init__(self):
        print("C")

class D(B,C):
    def __init__(self):
        print("D")

