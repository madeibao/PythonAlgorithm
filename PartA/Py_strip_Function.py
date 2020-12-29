碰到一个字符串的strip()用法，网上搜了一圈各种不懂（发现程序员们经常语体教），于是找人问了问。。。。
我在这里总结一下：
假设str是一个字符串
那么str.strip()就是把这个字符串头和尾的空格，以及位于头尾的"\n \t"之类给删掉。
举例e.g.1
str="  ABC"
那么str.strip() 就会为"ABC"
e.g.2
str="\t   AABBc  "
那么str.strip()就会为"AABBc"
e.g.3
str="  \n A BC \t"
那么str.strip()就会为"A BC"




















