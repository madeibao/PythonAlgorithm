


class Solution:
    def generateTheString(self, n: int) -> str:
            if n%2==1:
                return n*"a"
            else:
                return 1*"a"+(n-1)*"b"


