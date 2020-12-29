
# # # 第二题的程序的结果值
# 有bug，亟待解决。


# #第一个函数用来进行匹配关键字的结果值。
# # "read[addr=0x17,mask=0xff,val=0x7]"

# def spp(str2, read):
# 	a = str2.index("[")

# 	temp = str2[:a]
# 	if temp!=read:
# 		return False
# 	return True



# # "addr=0x17,mask=0xff,val=0x7"
# # 输出['0x17', '0xff', '0x7']

# def rig(str2):
# 	list2 = str2.split(",")

# 	# 三个变量的值

# 	a = list2[0]
# 	b = list2[1]
# 	c = list2[2]

# 	# 标志性的符号
# 	temp = "="

# 	indexa = a.index(temp)


# 	aa = a[indexa+1:]
# 	bb = b[indexa+1:]	
# 	cc = c[indexa:]  # C的开始位置比较特殊


# 	res = []

# 	res.append(aa)
# 	res.append(bb)
# 	res.append(cc)

# 	return res
# 	# ['0x17', '0xff', '0x7']

# if __name__ == "__main__": 
# 	str2 = input()

# 	# 长度值不能过大

# 	if(len(str2)>1024):
# 		print("FAIL")

# 	# 英文的字母范围
# 	list2 = list(str2)

# 	for i in range(len(list2)):
# 		if ord(list2[i])<0 or ord(list2[i])>128:
# 			print("FAIL")

# 	a,b = str2.strip().split(" ")

# 	# 分割所有的字符串的内
# 	list3 = b.split("],")

# 	# 去除最后的一个位置的

# 	list3[-1].replace("]","")

# 	print(list3[-1])


# 	# for i in range(len(list3)):
# 	# 	res =[]
# 	# 	# 关键字大小不匹配
# 	# 	if(spp(i,a)==False):
# 	# 		continue
# 	# 	else:
# 	# 		res.append(rig(i))

# 	# for i in res:
# 	# 	for j in i:
# 	# 		print(j[0]+" "+j[1]+" "+j[2])

# 	# 	print("\n")
# # 网上的答案：

# 第二题：字符串匹配

# 输入：
# read read[addr=0x17,mask=0xff,val=0x7],read_his[addr=0xff,mask=0xff,val=0x1],read[addr=0xf0,mask=0xff,val=0x80]
# 输出：
# 0x17 0xff 0x7
# 0xf0 0xff 0x80


# 作者：孤独时代的飞行员
# 链接：https://www.nowcoder.com/discuss/409163
# 来源：牛客网



# ----------------------------------------------------------------------------------------------------------------

import sys
 
def fun():
    # 首先来进行字符串的分割参数。
    key_word, words = sys.stdin.readline().strip().split(" ")
    res = []
    words = words.split("],")
    # 最后的一个字符串的结果之来进行截取，最后的一个字符特殊的来进行处理。
    words[-1] = words[-1][:-1]
    # 然后遍历列表的结果值，找到对应的索引。
    for each in words:
        # 找出分隔符所对应的索引的位置结果值。
        index = each.find('[')
        key = each[:index]
        each = each[index + 1:]

        # 只有关键字对应的条件下才能够进行匹配的操作，否则不会进行。
        if key == key_word:

        	# 划分三个部分的内容。
            addr, mask, val = each.split(",")

            # 第一个关键字的值为五个字符的值，第二个5个，第三个四个字符。
            addr_info = addr[5:]
            mask_info = mask[5:]
            val_info = val[4:]

            # 首先来捕获异常的需求。
            try:
                _ = int(addr_info, base=16)
                _ = int(mask_info, base=16)
                _ = int(val_info, base=16)
                res.append([addr_info, mask_info, val_info])
            except ValueError:
                continue

    if len(res) == 0:
        print("FAIL")
    for each in res:
        print(" ".join(each))
 
if __name__ == '__main__':
    fun()













