


while True:
    try:
        k=input()
        for a in range(21):
            for b in range(33):
                c=(100-a*5-b*3)*3
                if 5*a+3*b+c/3==100 and c>=0 and a+b+c==100:
                    print(str(a)+' '+str(b)+' '+str(c))
    except:
        break






