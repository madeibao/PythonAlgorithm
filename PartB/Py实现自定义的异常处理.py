


class MyException(Exception):
    pass
 
try:
    phone_num = input("请输入手机号：")
 
    if phone_num.isdecimal() is False:
        #print("手机号码含非数字")
        raise MyException("手机号码含非数字")
    elif len(phone_num) != 11:
        # print("手机号长度不够")
        raise MyException("手机号长度不够")
except MyException as error:
    print("提示：%s" % error)
 
 
结果：
请输入手机号：sgvsdfgsgsgsdgds
提示：手机号码含非数字