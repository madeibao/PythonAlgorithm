


# python的字符串的匹配的操作，
# 判断短字符串中的所有的字符是否都出现在较长的字符串中。


while True:
    try:
        a,b=set(input()),set(input())
        print ("true" if a&b==a else "false")
    except:
        break

