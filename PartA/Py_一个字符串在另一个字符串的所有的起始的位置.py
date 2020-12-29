

def find(substr, string):
    startpos=0
    occu=[]
    while True:
        result = string.find(substr, startpos)
        if result == -1:
            break
        else:
            occu.append(result)
            startpos = result+len(substr)

    list2 = [str(i) for i in occu]
    list3 = ' '.join(list2)
    return list3


if __name__ == '__main__':
    print(find("vivo", "avivobedecwefvivoabcdvivo"))



# 一个字符串在另一个字符串中的所有的起始的位置。









