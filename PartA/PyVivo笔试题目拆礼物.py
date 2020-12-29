

#vivo的拆礼物的算法结果值。
#问最多需要拆去多少层的礼品盒子。

def solution(s):
    count = 0
    for i in s:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        elif i == "0":
            break
    return count

if __name__ == '__main__':
    input = input()
    print(solution(input))
