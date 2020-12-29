append用法list.append（x），也就是将某个元素x追加到已知的一个列表的尾部。

注意：在append（）括号中写数字不用加引号，中文和字母都要加引号

list[1,2,3,4]
list.append(34)
print(list)
#输出结果：
[1,2,3,4,34]



extend用法list.extend(b)

有两个list，一个是list，另外一个是b，将b这个列表extend到list的后面，也就是把b中的所有元素加入到list中，即让list扩容。

list=[1,2,3]
b=[4,5,6]
list.extend(b)
print(list）
#输出结果：
[1,2,3,4,5,6]


list=[1,2,3]
b=[4,5,6]
list+=b
print(list)



————————————————
版权声明：本文为CSDN博主「qq_41936849」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_41936849/article/details/81018566