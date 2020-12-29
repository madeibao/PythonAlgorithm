


def replaceSame(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    hashTable1 = {}
    hashTable2 = {}
    for i in range(65, 91):
        hashTable1[i] = 0
        hashTable2[i] = 0
    for i in range(97, 123):
        hashTable1[i] = 0
        hashTable2[i] = 0
    for i in list1:
        hashTable1[ord(i)] += 1
    for i in list2:
        hashTable2[ord(i)] += 1
    for i in list1 if len(list1)>=len(list2) else list2:
        if hashTable1[ord(i)]>0 and hashTable2[ord(i)]>0:
            list1[list1.index(i)] = '_'
            list2[list2.index(i)] = '_'
    print("".join(list1))
    print("".join(list2))

    
def judge(str1, str2):
    if len(str1)>10 or len(str2)>10:
        print('请输入长度不超过100的字符串')
        return False
    elif str1=="" or str2=="":
        print('字符串不能为空')
        return False
    for j in a:
        if 65<=ord(j)<=90 or 97<=ord(j)<=122:
            continue
        else:
            print('请输入只包含字母的字符串')
            return False
    return True


if __name__ == '__main__':
    a = input("a=")
    b = input("b=")
    if judge(a, b):
        replaceSame(a, b)