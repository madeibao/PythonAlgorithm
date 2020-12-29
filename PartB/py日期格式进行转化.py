



class Solution:
    def reformatDate(self, date: str) -> str:
        # 月份字典
        dic_m = dict(zip(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], list(range(1,13))))
        
        # date字符分割转列表
        date = date.split(' ')

        # day格式转换
 
        #如果是    6th   这种样式的内容.
        if len(date[0]) == 3:
            date[0] = '0' + date[0][0]
        else:
            date[0] = date[0][0:2]

           			# > 号码的写法是右对齐的格式来进行。
        return f"{date[2]}-{2:0>2}-{date[0]}"


if __name__ == '__main__':
	s =Solution()
	date = "6th Jun 1933"
	print(s.reformatDate(date))