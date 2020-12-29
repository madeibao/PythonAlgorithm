




class Solution: # 双栈 存索引
    def checkValidString(self, s: str) -> bool:
        left,star=[],[]
        for i,c in enumerate(s):
            if c == '(': left.append(i)
            elif c == '*': star.append(i)
            else:
                if left: left.pop()
                elif star: star.pop()
                else: return False;
        while  left and  star :
            if left.pop() > star.pop(): return False
        return not left


if __name__ == '__main__':
	s =Solution()
	print(s.checkValidString("(*)"))

	