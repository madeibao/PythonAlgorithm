
# 给定数字列表，然后返回的是这个数字来组成的一个最大的数字


class Solution(object):
    def largest(self,nums):
        from functools import cmp_to_key
        def helper(x, y):
            if x+y>y+x:
                return -1
            elif x+y<y+x:
                return 1
            else:
                return 0

        return "".join(sorted(map(str, nums),key=cmp_to_key(helper))).lstrip("0") or "0"


if __name__ == "__main__":
    s = Solution()
    print(s.largest([2,3,23,3,4]))




    