


import re
class Solution:
    def validIPAddress(self, IP: str) -> str:

        pattern_ipv4 = "^((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$"
        pattern_ipv6 = "^([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}$"
        m_ipv4 = re.compile(pattern=pattern_ipv4)
        m_ipv6 = re.compile(pattern=pattern_ipv6)
        if m_ipv4.match(IP):
            return "IPv4"
        elif m_ipv6.match(IP):
            return "IPv6"
        else:
            return "Neither"


if __name__ == "__main__":
    s = Solution()
    str2 = "172.16.254.1"
    print(s.validIPAddress(str2))

