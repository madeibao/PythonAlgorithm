a = 4
print(isinstance (a,int)) # True
print(isinstance (a,str)) # False
print(isinstance (a,(str,int,list)))  # 对于这种元组的表示情况，只要后面有一种情况满足就返回为真。


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))   # returns True
print(type(A()) == A)       # returns True
print(isinstance(B(), A))   # returns True
print(type(B()) == A)       # returns False

