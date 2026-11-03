

# 这里是回溯解法，更简洁优雅。

from typing import List

class Solution:
    def validIp(self, t: str) -> bool:
            if not t:
                return False
            if (len(t) > 4) or (len(t) > 1 and t[0] == "0"):
                return False
            num = int(t)
            return num <= 255 and num >= 0

    def restoreIpAddresses(self, s: str) -> List[str]:
        """将数字字符串还原为所有可能的合法 IP 地址。

        使用回溯（DFS）将字符串切分为 4 段，每段长度 1~3，
        并通过 validIp 校验每段是否合法（无前导零、数值在 0~255 之间）。

        Args:
            s: 仅由数字组成的字符串。

        Returns:
            所有可能的合法 IP 地址列表，每个地址以 "." 分隔四段；
            若无法还原则返回空列表。
        """
        ans = []
        def dfs(s, path):
            # 已切出 4 段：剩余字符串为空则是一个合法结果，否则剪枝返回
            # 这里不能用len(path)==4 and not s: 这种写法，因为如果len(path)==4但s不为空，仍然需要返回而不是继续切分
            if len(path) == 4:
                if not s:
                    ans.append(".".join(path))
                return
            # 每段长度只能是 1~3，且不能超过剩余字符数
            for i in range(1, 4):
                if i <= len(s):
                    t = s[:i]  # 取当前这一段
                    if self.validIp(t):
                        # 当前段合法，继续切分剩余字符串
                        dfs(s[i:], path + [t])
        dfs(s, [])
        return ans

if __name__ == "__main__":
    s = "25525511135"
    solution = Solution()
    print(solution.restoreIpAddresses(s))
