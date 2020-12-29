
class Stack:

    def __init__(self,limit=10):#初始化，栈的最大范围默认是10

        #变量名字前有两条下划线，说明是私有变量

        self.__stack=[]

        self.__limit=limit

    def __str__(self):#使用print的时候直接调用

        return ''.join([str(i) for i in self.__stack])

    def push(self,data):#入栈

        if len(self.__stack)>=self.__limit:

            self.double_limit()#如果栈的范围不够就扩大一倍

        self.__stack.append(data)

    def pop(self):#出栈

        if len(self.__stack)<=0:

            return -1

        else:

            self.__stack.pop()#调用python列表自带的pop

    def peek(self):#返回栈顶的元素

        if len(self.__stack)<=0:

            return -1

        else :

            return self.__stack[-1]

    def is_empty(self):#判断是否为空

        return self.size()==0

    def size(self):

        return len(self.__stack)    # 返回栈的大小。

    def double_limit(self):

        self.__limit*=2

#示例代码

mystack=Stack()

for i in range(10):

    mystack.push(i)

print(mystack)

mystack.pop()

print(mystack)

print(mystack.peek())
