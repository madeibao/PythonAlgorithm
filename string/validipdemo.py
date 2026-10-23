class Solution:
    @staticmethod
    def valid_segment(seg: str) -> bool:
        """判断一段是否合法：长度 1~3、无前导零（"0" 本身除外）、数值不超过 255。"""
        n = len(seg)
        if n == 0 or n > 3:
            return False
        if n > 1 and seg[0] == "0":
            return False
        return n < 3 or int(seg) <= 255  # 1~2 位最大 99，无需转换

    def restoreIpAddresses(self, s: str) -> list[str]:
        n = len(s)
        # 合法 IP 共 4 段、每段 1~3 位，总长必在 [4, 12]，否则直接无解
        if n < 4 or n > 12:
            return []

        ans = []
        for a in range(1, 4):                 # 第 1 段长度
            s1 = s[:a]
            if not self.valid_segment(s1):
                break
            if not 3 <= n - a <= 9:           # 剩余 3 段共需 3~9 个字符
                continue
            for b in range(1, 4):             # 第 2 段长度
                s2 = s[a:a + b]
                if not self.valid_segment(s2):
                    break
                if not 2 <= n - a - b <= 6:   # 剩余 2 段共需 2~6 个字符
                    continue
                for c in range(1, 4):         # 第 3 段长度
                    s3 = s[a + b:a + b + c]
                    if not self.valid_segment(s3):
                        break
                    s4 = s[a + b + c:]        # 第 4 段，长度是否 1~3 由 valid_segment 兜底
                    if self.valid_segment(s4):
                        ans.append(f"{s1}.{s2}.{s3}.{s4}")
        return ans


if __name__ == "__main__":
    sol = Solution()
    for case in ("25525511135", "0000", "101023", "010010", "123", "1" * 13):
        print(f"{case!r} -> {sol.restoreIpAddresses(case)}")
