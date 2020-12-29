

class Solution:
    def checkValidString(self, s: str) -> bool:
        lo=0
        hi=0
        for c in s:
            if c=='(':
                lo+=1
                hi+=1
            elif c=='*':
                if lo>0:lo-=1
                hi+=1
            else:
                if lo>0:lo-=1
                hi-=1
            if hi<0:
                return False
        return lo==0


class Solution {
    public boolean checkValidString(String s) {
        int lNum = 0;//从左往右扫描，若是'(' 则加1 若是')'则减1
        int rNum = 0;//从右往左扫描，若是')' 则加1 若是'('则减1
        int lSum = 0;//从左往左扫面，*的个数
        int rSum = 0;//从右往左扫描，*的个数
        int len = s.length();
        for(int i = 0; i < s.length(); i ++){
            if(s.charAt(i) == '(') //从左往右扫描开始
                lNum ++;
            else if(s.charAt(i) == ')')
                lNum --;
            else
                lSum ++;
            if(lNum + lSum < 0) //若')'这个数量大于'('这个数量 lNum 则为负数 切*的数量少于这个数量，则不能满足字符串要求
                return false;

            len --; //从右扫描的起点
            if(s.charAt(len) == ')')//从右往左扫描。与上同理
                rNum ++;
            else if(s.charAt(len) == '(')
                rNum --;
            else
                rSum ++;
            if(rNum + rSum < 0)
                return false;  
        }
        if(lSum < lNum || rSum < rNum)//从左往右或者从右往左，* 的数量少于括号则不能完成匹配
            return false;
        return true;
    }
}
class Solution:
    def checkValidString(self, s: str) -> bool:
        lNum = 0 #//从左往右扫描，若是'(' 则加1 若是')'则减1
        rNum = 0 #//从右面往左面扫描，若是')' 则加1 若是'('则减1
        lSum = 0 # 从左往右面扫面，*的个数
        rSum = 0 # 从右面往左扫面，*的个数


        leng = len(s)
        for i in range(0,leng):
            if '(' == s[i]:
                lNum += 1
            elif ')' == s[i]:
                lNum -= 1
            else :
                lSum += 1
            if lNum + lSum< 0:
                return False
            
            leng -= 1
            if '(' == s[leng]:
                rNum -= 1
            elif ')' == s[leng]:
                rNum += 1
            else :
                rSum += 1
            if rNum + rSum < 0:
                return False
                
        if (lSum < lNum) or (rSum < rNum):
            return False
        return True


#----------------------------------------------------------------
#----------------------------------------------------------------

if __name__=='__main__': 
    s = Solution()
    print(s.checkValidString("(*)"))