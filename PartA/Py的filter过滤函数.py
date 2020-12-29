

python-filter函数 

filter
1、循环帮你调用函数
2、帮你过滤你传入的参数，函数的结果返回的是true那就保存，返回false就不要，且返回的也是迭代器
 
备注：迭代器用完一个就扔掉一个，直到全部用完，且需要一个list接一下，否则返回的是对象
 
格式： filter(function, iterable)
          function -- 判断函数
          iterable -- 可迭代对象

def add(a):
    return a%2==0

print(list(filter(add,[1,2,3,4])))


[2,4]
# ----------------------------------------------------------------
# ----------------------------------------------------------------



stu_score = {'xiaobai': 50, 'xiaohei': 30, 'xiaolan': 80, 'xiaojun': 100, 'xiaoming': 60}

result = filter(lambda score: score > 60, stu_score.values())
print(list(result))

#================================================================

[100, 80]
