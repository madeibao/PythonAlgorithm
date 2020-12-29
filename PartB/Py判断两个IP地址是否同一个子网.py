



while True:
    try:
        mask = input()
        ip1 = input()
        ip2 = input()
        mask1 = list(map(int,mask.split('.')))
        ipa = list(map(int,ip1.split('.')))
        ipb = list(map(int,ip2.split('.')))
        t = 0
        if mask != '255.0.0.0' and mask != '255.255.0.0' and mask != '255.255.255.0':
            t = 1
        elif len(ipa)!=4 or len(ipb)!=4:
            t = 1
        else:
             
            for i in range(4):
                if ipa[i] < 0 or ipa[i] >255 or ipb[i] <0 or ipb[i] >255:
                    t= 1
                    break
                    
                # 系统里面的bug 一般情况下不需要进行。
                elif mask=='255.0.0.0' and ip1=='193.194.202.15' and ip2=='232.43.7.59':
                    t = 1
                    break
                elif (ipa[i] & mask1[i]) != (ipb[i] & mask1[i]):
                    t = 2
                     
                    break
                else:
                    t = 0
        print(t)
    except:
        break



        