
'''

自守数是指一个数的平方的尾数等于该数自身的自然数。例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376。请求出n以内的自守数的个数 
输入一个数字，判断这个范围内的自守数字的个数。
'''

# 求n以内的自守的数字


while True:
    try:
        def isnum(num):
            num3 = num * num

            str2 = str(num)
            len2 = len(str2)
            str3 = str(num3)
            len3 = len(str3)
            str4 = str3[len3 - len2:]
            num4 = int(str4)

            if num4 == num:
                return True
            else:
                return False
        n = int(input())
        count = 0
        for i in range(n+1):
            if isnum(i):
                count += 1
        print(count)
    except:
        break



