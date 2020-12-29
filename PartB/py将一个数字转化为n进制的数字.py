

# 输入一个数字，然后转化为另一个n进制的数字




input_list = [int(i) for i in input().strip().split(' ')]
#print(input_list)
M, N = input_list[0],input_list[1]
jz = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

flag = ''
if M < 0:
    flag = '-'
    M = -1 * M
if M == 0:
    print('0')
res= ''
while M != 0:
    chu = M%N
    res = jz[chu] + res
    M = M//N
print(flag+res)
    
    