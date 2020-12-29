



ans = [1, 2, 3, 4, 7]
ans2 = ans
print(ans)
ans2[3] = 15
print(ans)



ans 和ans2 都共同的指向了一个列表的内容。

所以当ans2变化的时候，ans也会同时进行变化。


最终的结果为：



[1, 2, 3, 4, 7]
[1, 2, 3, 15, 7]























