


def hi(name="yasoob"):
    return "hi " + name


print(hi())
# output: 'hi yasoob'

# 我们甚至可以将一个函数赋值给一个变量，比如
greet = hi
# 我们这里没有在使用小括号，因为我们并不是在调用hi函数
# 而是在将它放在greet变量里头。我们尝试运行下这个

print(greet())
# output: 'hi yasoob'

# 如果我们删掉旧的hi函数，看看会发生什么！
del hi
print(hi())
# outputs: NameError

print(greet())
# outputs: 'hi yasoob'



# ================================================================================================================================
在函数中来定义函数的值：

def hi(name="yasoob"):
    print("now you are inside the hi() function")
 
    def greet():
        return "now you are in the greet() function"
 
    def welcome():
        return "now you are in the welcome() function"
 
    print(greet())
    print(welcome())
    print("now you are back in the hi() function")
 
hi()
#output:now you are inside the hi() function
#       now you are in the greet() function
#       now you are in the welcome() function
#       now you are back in the hi() function
 
# 上面展示了无论何时你调用hi(), greet()和welcome()将会同时被调用。
# 然后greet()和welcome()函数在hi()函数之外是不能访问的，比如：
 
greet()
#outputs: NameError: name 'greet' is not defined




从函数中返回函数
其实并不需要在一个函数里去执行另一个函数，我们也可以将其作为输出返回出来：

def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"
 
    def welcome():
        return "now you are in the welcome() function"
 
    if name == "yasoob":
        return greet
    else:
        return welcome
 
a = hi()
print(a)
#outputs: <function greet at 0x7f2143c01500>
 
#上面清晰地展示了`a`现在指向到hi()函数中的greet()函数
#现在试试这个
 
print(a())
#outputs: now you are in the greet() function
再次看看这个代码。在 if/else 语句中我们返回 greet 和 welcome，而不是 greet() 和 welcome()。为什么那样？
这是因为当你把一对小括号放在后面，这个函数就会执行；然而如果你不放括号在它后面，那它可以被到处传递，并且可以赋值给别的变量而不去执行它。 你明白了吗？让我再稍微多解释点细节。

当我们写下 a = hi()，hi() 会被执行，而由于 name 参数默认是 yasoob，所以函数 greet 被返回了。
如果我们把语句改为 a = hi(name = "ali")，那么 welcome 函数将被返回。
我们还可以打印出 hi()()，这会输出 now you are in the greet() function。


# ================================================================ ==============	===================


# 第一个装饰器的例子。
def a_new_decorator(a_func):
 
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
 
        a_func()
 
        print("I am doing some boring work after executing a_func()")
 
    return wrapTheFunction
 
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")
 
a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell"
 
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#now a_function_requiring_decoration is wrapped by wrapTheFunction()
 
a_function_requiring_decoration()
#outputs:I am doing some boring work before executing a_func()
#        I am the function which needs some decoration to remove my foul smell
#        I am doing some boring work after executing a_func()



#================================================================================================================================
from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")


a_function_requiring_decoration()