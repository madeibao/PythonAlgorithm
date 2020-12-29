
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b=int(a,2),int(b,2)
        ans=bin(a+b)
        ans=str(ans)
        ans=ans[2:]
        return ans

# 先把 a,b用bin(数，原本的进制)转为二进制
# 得到a+b的二进制数
# 将二进制数转为字符串
# 截取字符串的索引为2的元素到最后（前两位为0b所以要截取）

cc= Solution()
print(cc.addBinary("1011","1101"))




# 根据输入内容来确定两个字符串的相加。


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b=int(a,2),int(b,2)
        ans=bin(a+b)
        ans=str(ans)
        ans=ans[2:]
        return ans

# 先把 a,b用bin(数，原本的进制)转为二进制
# 得到a+b的二进制数
# 将二进制数转为字符串
# 截取字符串的索引为2的元素到最后（前两位为0b所以要截取）


cc = Solution()
b = input().split()  # 依次输入这些数据。  # 这样也可以一次的输入一些数据。
print(cc.addBinary(b[0], b[1]))











