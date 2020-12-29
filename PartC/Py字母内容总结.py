

 048      060   030   00110000        0         
 049      061   031   00110001        1         
 050      062   032   00110010        2         
 051      063   033   00110011        3         
 052      064   034   00110100        4         
 053      065   035   00110101        5         
 054      066   036   00110110        6         
 055      067   037   00110111        7         
 056      070   038   00111000        8         
 057      071   039   00111001        9



0 的 码是48
9 的 码是57

A 的 码是65

Z 的 码是90

a 的 码是97

z 的 码是122



判断是字符是否为数字 ord(c)  给出一个字符的ASCII 码
给定一个数字内容，返回对应的ASCII 字符内容
chr(122)  得到的结果为  z


#============================================================

str_1 = "123"
str_2 = "Abc"
str_3 = "123Abc"

#用isdigit函数判断是否数字
print(str_1.isdigit())
Ture
print(str_2.isdigit())
False
print(str_3.isdigit())
False

#用isalpha判断是否字母
print(str_1.isalpha())    
False
print(str_2.isalpha())
Ture    
print(str_3.isalpha())    
False

#isalnum判断是否数字和字母的组合
print(str_1.isalnum())    
Ture
print(str_2.isalnum())
Ture
print(str_1.isalnum())    
Ture
注意：如果字符串中含有除了字母或者数字之外的字符，比如空格，也会返回False




