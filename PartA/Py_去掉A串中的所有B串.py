def removeSubstring(str1,str2):
    # return str1.replace(str2,'')
    while str1.find(str2)!=-1:
        str1 = str1[:str1.find(str2)] + str1[str1.find(str2)+len(str2):]
    return str1

if __name__ == '__main__':
   str1 = 'abcdefgabcdefgbcb'
   str2 = 'bc'
   print(removeSubstring(str1,str2)) # adefgadefgb



   