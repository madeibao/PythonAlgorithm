# 密码要求:
# 1.长度超过8位
# 2.包括大小写字母.数字.其它符号,以上四种至少三种
# 3.不能有相同长度超2的子串重复
# 说明:长度超过2的子串


def islegal2(s):
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    for ss in s:
        if 'a' <= ss <= 'z':
            num1 = 1
        elif 'A' <= ss <= 'Z':
            num2 = 1
        elif '1' <= ss <= '9':
            num3 = 1
        else:
            num4 = 1
    if (num1 + num2 + num3 + num4) >= 3:
        return True
    else:
        return False


def fun3(s):
    for i in range((len(s)-3)):
        if s[i:i+3] in s[i+1:]:    # 长度超过2的子串重复的出现在后续的字符串中。
            return False
            break
    return True


def lenpan(str2):
    if len(str2) > 8:
        return True
    else:
        return False


while True:
    try:
        str2 = input()
        if lenpan(str2) and islegal2(str2) and fun3(str2):
            print("OK")
        else:
            print("NG")
    except:
        break

