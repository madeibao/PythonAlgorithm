
# 100 150
# 判定一个区间内容的回文素数的值。
# 不仅是回文数字，而且是素数的数字。



import math

def is_prime_and_palindrome(n):
    if str(n) != str(n)[::-1]:
        return False
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True



if __name__ == "__main__":
    start, end = map(int, input().split())

    # 过滤器其中的结果值。
    # filter的参数后面的是一个可循环的迭代器内容。
    print(len(list(filter(lambda c: is_prime_and_palindrome(c), range(start, end + 1)))))