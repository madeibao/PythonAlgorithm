1.3 使用f-Strings格式化字符串
Python有很多不同的方法来处理字符串格式化，
有时候不知道使用哪个
f-strings支持使用字符串格式化迷你语言，以及强大的字符串插值。
这些功能允许添加变量甚至有效的Python表达式，并在添加到字符串之前在运行时对它们进行评估。



def get_name_and_decades(name, age):
    return f"My name is {name} and I'm {age} years old."

print(get_name_and_decades("Maria", 31))
