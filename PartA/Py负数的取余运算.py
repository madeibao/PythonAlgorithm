负数取余/整除，Python和C语言的不同 

总结一句：Python中负数整除，是向负无穷取整，所以导致负数取余不对
在数学公式中，两种语言的表示算法都是一样的，都是：
r=a-n*[a/n]
以上，r是余数，a是被除数，n是除数。
唯一不同点，就是商向0或负无穷方向取整的选择，c从c99开始规定向0取整，python则规定向负无穷取整，选择而已。
向零取值的含义是：9/7=1 .29----向0取值-->1；-9/7=-1.29----向0取值------>-1
向负无穷取值的含义是：9/7=1 .29----向0取值-->1；-9/7=-1.29----向0取值------>-2
所以套用上述公式为：
C 语言：（a%n的符号与a相同）
            -9%7=-9 - 7*[-1]=-2；
            9%-7=9 - -7*[-1]=2;
Python语言：：（a%n的符号与n相同）
            -9%7=-9 - 7*[-2]=5
            9%-7=-9 - -7*[-2]=-5

#----------------------------------------------------------------



在Python中，取余的计算公式与别的语言并没有什么区别：r=a-n*[a//n]
这里r是余数，a是被除数，n是除数。
不过在“a//n”这一步，当a是负数的时候，我们上面说了，会向下取整，也就是说向负无穷方向取整。这也就得到：
-123%10 = -123 - 10 * (-123 // 10) = -123 - 10 * (-13) = 7