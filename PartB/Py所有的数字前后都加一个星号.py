# 字符中所有出现的数字前后加上符号“*”，其他字符保持不变

# Jkdi234klowe90a3
# Jkdi*234*klowe*90*a*3*
# 输出结果为


while True:
    try:
        str2 = input()
        list2 = list(str2)
        str3 = str()   # 建立一个空的字符串。
        for i in list2:
            if i >= '0' and i <= '9':
                str3 += "*" + i + "*"
            else:
                str3 += i

        str4 = str3.replace("**", "")
        print(str4)
    except:
        break

