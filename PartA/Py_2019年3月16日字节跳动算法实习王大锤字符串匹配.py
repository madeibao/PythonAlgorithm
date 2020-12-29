


题目描述：（1）三个同样的字母连在一起，一定是拼写错误，去掉一个就好了，比如：helllo->hello；
         （2）两对一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的一个字母就好了：比如：helloo->hello；
         （3）上面的规则优先“从左到右匹配”，即如果是AABBCC，虽然AABB和BBCC都是错误拼写，应该优先考虑修复AABB，结果为AABCC

输入描述：第一行包括一个数字N，表示本次用例包括多少个待校验的字符串。后面跟随N行，每行为一个待校验的字符串。

输出描述：N行，每行包括一个被修复后的字符串。
举例：

输入：   2
        helloo
        wooooooow

输出：hello

      woow   


#字符串修正函数

def correction_string(s):

    n = len(s)
    r = list(s[:min(len(s), 2)])
    for i in range(2, n):
        if s[i] == r[-1] == r[-2]:
            continue
        if s[i] == r[-1] and len(r) > 2 and r[-2] == r[-3]:
            continue
        r.append(s[i])

    new_string = ''.join(r)
    return new_string


for i in range(int(input())):

    s=input()

    print(correction_string(s))
