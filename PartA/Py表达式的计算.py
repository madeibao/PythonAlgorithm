


# 给定一个表达式，求出表达式的值。


# 例如："3+2*{1+2*[-4/(8-6)+7]}"


while True:
    try:
        s = input()
        str2 = s.replace("{", "(")
        str3 = str2.replace("[", "(")
        str4 = str3.replace("}", ")")
        str5 = str4.replace("]", ")")
        print(int(eval(str5)))
    except:
        break



