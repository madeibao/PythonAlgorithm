给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。

注意：1 ≤ k ≤ n ≤ 109。

示例 :

输入:
n: 13   k: 2

输出:
10

解释:
字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def cal_steps(n, n1, n2):
            step = 0
            while n1 <= n:
                step += min(n2, n + 1) - n1
                n1 *= 10
                n2 *= 10
            return step
                
        cur = 1
        k -= 1
        
        while k > 0:
            steps = cal_steps(n, cur, cur + 1)
            if steps <= k:
                k -= steps
                cur += 1
            else:
                k -= 1
                cur *= 10
        
        return cur


if __name__ == "__main__":
	s = Solution()
	print(s.findKthNumber(13, 2))
