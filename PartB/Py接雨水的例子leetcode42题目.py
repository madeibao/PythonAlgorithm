

# leetcode的接雨水题目

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res, hei_len, peak = 0, len(height), 0
        # 如果只有两根柱子是没有办法接到雨水的。而且位置相邻的话，是没有办法接到雨水的。
        if hei_len < 3:
            return 0

        max_val = height[0]   # 最大的值为假定的第一个位置。
        for i in range(1, hei_len):
            if height[i] >= max_val:
                max_val = height[i]
                peak = i              # 获取最大的高度值和所在的顶峰的位置值。


        max_left, max_right = height[0], height[-1]
        for i in range(peak):
            print("左面的最大值", max_left)
            if max_left < height[i]:
                max_left = height[i]
            else:
                res += max_left - height[i]

        for i in range(hei_len - 1, peak, -1):
            if max_right < height[i]:
                max_right = height[i]
            else:
                res += max_right - height[i]

        return res


if __name__ == "__main__":
    s = Solution()
    height = list(map(int, input().split(",")))
    print(s.trap(height))




#  0,1,0,2,1,0,1,3,2,1,2,1