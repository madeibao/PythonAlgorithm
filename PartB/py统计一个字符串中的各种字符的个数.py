

# 1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\][
# 

# 26
# 3
# 10
# 12


#----------------------------------------------------------------------------


while True:
    try:
        str1 = input()
        a = 0
        space = 0
        num = 0
        other = 0
        for i in str1:
            if i.isdigit():
                num+=1
            elif i.isalpha():
                a+=1
            elif i == ' ':
                space+=1
            else:
                other += 1
        print(a)
        print(space)
        print(num)
        print(other)
    except:
        break


