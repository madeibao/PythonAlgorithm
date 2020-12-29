
class Solution:
    def countLargestGroup(self, n: int) -> int:

        # mx用来统计数组中的出现最多的组的值。
        cnt, mx, res = collections.defaultdict(int), 0, 0
        for i in range(1, n + 1):
            t = sum([int(j) for j in str(i)])
            cnt[t] += 1
            mx = max(mx, cnt[t])
        return sum([i == mx for i in cnt.values()])


if __name__ == "__main__":
    s = Solution()
    n = 14
    print(s.countLargestGroup(n))

