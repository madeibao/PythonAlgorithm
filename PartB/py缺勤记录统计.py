
'''
给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。

你需要根据这个学生的出勤记录判断他是否会被奖赏。

示例 1:

输入: "PPALLP"
输出: True

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/student-attendance-record-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A')>1:
            return False
        for i in range(len(s)-2):
            if s[i]=='L' and s[i+1]=='L' and s[i+2]=='L':
                return False
        return True



if __name__=='__main__': 
    s = Solution()
    str2 = "PPALLP"
    print(s.checkRecord(str2))

