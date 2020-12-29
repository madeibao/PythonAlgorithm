

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.strip()
        flag = ''
        if len(str)==0:
            return 0
        if len(str)==1:
            if '9'>=str>='0':
                return int(str)
            else:
                return 0

        if str[0] in '-+':
            flag=str[0]
            # 截取其中的字符串的内容。
            str=str[1:]

        result = ''
        for i in str:
            if '9'>=i>='0':
                result+=i
            else:

            	# 如果有非法的字符，就直接的终止结果值。
                break

        if result=='':
            return 0 
        else:
            result = flag+result
            
        if -2**31<=int(result)<=2**31-1:
            return int(result)
        elif flag == '-':
            return -2**31
        else:
            return 2**31-1


if  __name__ == '__main__':	
	s = Solution()
	print(s.myAtoi("3232"))
