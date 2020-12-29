

# 河南村长，硬核宣传。
# 就你脸白就你脸香就你脸上抹点护手霜！


def No1(m,l):
	# 初始化默认的值。
    s='N'
    a=sorted(m)
    b=sorted(l)
    if a==b:
        s="Y"
    else:
        s="N"              
    return s
 
 
if __name__ == '__main__':
    n = input()
    n = int(n)
    s=[]   
    while n>0:
        m = input().split(' ')
        l = input().split(' ')
        m = list(map(int, m))
        l = list(map(int, l))
        a = No1(m,l)
        s.append(a)
        n-=1


    # 每次打印都要换行。
    for i in s:       
        print(i)






