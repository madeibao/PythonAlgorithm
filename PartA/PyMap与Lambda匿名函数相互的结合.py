


map(function, sequence[, sequence, ...]) -> list

Return a list of the results of applying the function to the items of
the argument sequence(s).  If more than one sequence is given, the
function is called with an argument list consisting of the corresponding
item of each sequence, substituting None for missing values when not all
sequences have the same length.  If the function is None, return a list of
the items of the sequence (or a list of tuples if more than one sequence).




function 为None 的情况



map(None, [1,2,3]) #[1, 2, 3]

map(None, [1,2,3], [4,5,6]) #[(1, 4), (2, 5), (3, 6)]

map(None, [1,2,3], [4,5]) 

#[(1, 4), (2, 5), (3, None)]



考虑function为lambda表达式的情形。
此时lambda表达式:的左边的参数的个数与map函数sequence的个数相等, :右边的表达式是左边一个或者多个参数的函数。

map(lambda x: x+1, [1,2,3]) #[2, 3, 4]

map(lambda x, y:x+y, [1,2,3], [4,5,6]) #[5, 7, 9]

map(lambda x, y:x == y, [1,2,3], [4,5,6]) #[False, False, False]

def f(x):
    return True if x==1 else Fasle
map(lambda x: f(x), [1,2,3]) #[True, False, False]


当lambda 为外部定义的函数的时候
def f(x):
    return True if x==1 else Fasle
map(f, [1,2,3]) #[True, False, False]






