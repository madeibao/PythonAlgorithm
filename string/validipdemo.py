
class Solution:
    def validIp(self, t:str)->bool:
        if len(t) > 3 or (len(t) > 1 and t[0] == '0'):
            return False
        res = int(t)
        if res<0 or res>255:
            return False
        return True

    def restoreIpAddresses(self, s: str) -> list[str]:
        ans = []
        for i in range(1, len(s)):
            if not self.validIp(s[:i]):
                break
            for j in range(i+1, len(s)):
                if not self.validIp(s[i:j]):
                    break
                for k in range(j+1, len(s)):
                    if not self.validIp(s[j:k]):
                        break
                    if self.validIp(s[k:]):
                        ans.append(f"{s[:i]}.{s[i:j]}.{s[j:k]}.{s[k:]}")
        return ans

if __name__=="__main__":
    s = "25525511135"
    s2 = Solution()
    print(s2.restoreIpAddresses(s))
