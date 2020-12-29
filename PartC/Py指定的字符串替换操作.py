
class Solution:    # s 源字符串
    def replaceSpace(self, s):
        # return "%20".join(list(s.split(" ")))
        return "%20",join(list(s.split(" ")))

c = Solution()
print(c.replaceSpace("I am the king of the world"))


# 结果为：
# I%20am%20the%20king%20of%20the%20world