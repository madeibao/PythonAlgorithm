
这是python3的新特性，简单理解为s:str中的s还是你要传的形参这个没有变，str为该形参的注释，意思是告诉你传入的s应该是个字符串，
当然这里重点理解一下注释二字，也就是说python仍然是动态赋值类型语言，这里虽然告诉你s应该是字符串，
但是你传一个int进去，你的代码也是可以正常跑的（前提是代码内部能正常处理该类型），
只不过如果你使用的IDE是pycharm这种的，会产生一些警告，而且这样的话注释也变的没有意义了。
而后面的-> int是return返回值的类型注释，
告诉你这个函数返回的是一个int类型，当然和参数注释一样，仅仅是注释。（官方文档PEP 3107 -- Function Annotations）

def testFunctionAnnotations(a: int, b: str) -> str:
    return str(a) + b


print(testFunctionAnnotations.__annotations__)
print(testFunctionAnnotations(123, "test"))
print(testFunctionAnnotations("123", "test"))


#----------------------------------------------------------------------------------------------

from typing import List, Tuple, Dict

def add(a:int, string:str, f:float, b:bool) -> Tuple[List, Tuple, Dict, bool]:

    list1 = list(range(a))

    tup = (string, string, string)

    d = {"a":f}

    bl = b

    return list1, tup, d, bl

print(add(5,"hhhh", 2.3, False))

# 结果：([0, 1, 2, 3, 4], ('hhhh', 'hhhh', 'hhhh'), {'a': 2.3}, False)





















