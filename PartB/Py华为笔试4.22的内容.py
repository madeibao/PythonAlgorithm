
# 作者：牛客168073942号
# 链接：https://www.nowcoder.com/discuss/414740?type=post&order=time&pos=&page=1&channel=
# 来源：牛客网

   V                          V              V                       V
# 5a 12 5b ba 34 5b bb 88 05 5a 75 cd bb 62 5a 34 cd 78 cc da fb 06 5a
# 5a 12 5b ba 34 5b bb 88 05 5a 34 cd 78 cc da fb 06 5a
#-----------------------------------------------------------------------------------------

strs = input().strip().split(" ")
last_flag=0

# 临时的列表结果值。
tmp_num=[]
# 临时的长度结果值。

tmp_length=0

# 最终的结果值。
res_list=["5a"]
i=1

while(i<len(strs)):
    print(tmp_num,res_list)
    if strs[i]=="5a":
        target_num=int(strs[i-1],16)
        #print(target_num,tmp_num)
        if tmp_length==target_num+1:
            res_list.extend(tmp_num.copy())
            res_list.append("5a")   
        last_flag=i
        tmp_num=[]
        tmp_length=0

    elif strs[i]=="5b":
        if i+1<len(strs):
            if strs[i+1]=="ba":
                tmp_num.append("5b")
                tmp_num.append("ba")
                tmp_length+=1
            elif strs[i+1]=="bb":
                tmp_num.append("5b")
                tmp_num.append("bb")
                tmp_length+=1
            i+=1
    else:
        tmp_num.append(strs[i])
        tmp_length += 1
    i+=1
 

for i in range(len(res_list)-1):
    print(res_list[i],end=" ")
print(res_list[-1])



