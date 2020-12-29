


定义和用法
index() 方法查找指定值的首次出现。
如果找不到该值，index() 方法将引发异常。

index() 方法与 find() 方法几乎相同，唯一的区别是，如果找不到该值，则 find() 方法将返回 -1。（请看下面的例子）

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)


