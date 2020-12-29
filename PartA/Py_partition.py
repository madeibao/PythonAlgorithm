

Python partition() 方法用来根据指定的分隔符将字符串进行分割。

如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符前面的子字符串，第二个为分隔符本身，第三个为分隔符后面的子字符串。

partition() 方法是在Python 2.5中新增的。




str2 = "http://www.w3cschool.cc/"


leftcontex, _, rightcontext = str2.partition("//")
print(leftcontex)
print(rightcontext)




















