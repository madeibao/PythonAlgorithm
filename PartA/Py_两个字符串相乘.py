

'''
                                    1      2     3
                        *           4      5     6
-----------------------------------------------------------------------
                                    6     12    18
                           5       10     15                    
                  4        8       12
-----------------------------------------------------------------------
          0       4       13      28      27    18


    最终结果为     5        6       0       8     8    (56088)

获得一个逆序的列表形式[18, 27, 28, 13, 4, 0]
                  
'''


class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        #  把num1,num2翻转方便计算
        num1 = num1[::-1]
        num2 = num2[::-1]
        #  每一位互相乘的结果用一维数组去储存
        arr = [0 for i in range(len(num1)+len(num2))]
        #  填充这个一维数组
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j] += int(num1[i]) * int(num2[j])   # 相乘的结果值。
        ans = []
        #  计算每一位的终极结果
        for i in range(len(arr)):
            #  digit表示这一位的数字
            digit = arr[i] % 10
            #  carry表示加给下一位的量
            carry = arr[i] // 10   # 取整除的算法。

            if i < len(arr)-1:
                #  下一位加上
                arr[i+1] += carry   # 进位
            #  更新答案
            ans.insert(0, str(digit))   # 一般都是头插法。 存储的是最终的答案。  注意添加的是字符串的形式。
        #  去除首位为0的情况



        while ans[0] == '0' and len(ans) > 1:
            del ans[0]   # 删除首位为0的情况。
        #  连接成字符串
        return ''.join(ans)


cc = Solution()
print(cc.multiply("123", "456"))












