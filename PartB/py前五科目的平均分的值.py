


import heapq
class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        record = dict()
        
        for item in items:
            sd, sc = item[0], item[1] #student, score
            
            if sd not in record:
                record[sd] = [sc]
                heapq.heapify(record[sd]) #初始化
            else:
                heapq.heappush(record[sd], sc) #新分入堆

                # 如果堆元素大于5  
                if len(record[sd]) > 5:
                    heapq.heappop(record[sd]) #六个分里最小的出堆
                    #print record[sd]
        
        res = []
        for key, val in record.items():
            res.append([key, sum(val) // 5])
        # print record
        return res


if __name__ == "__main__":
    s = Solution()
    items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    print(s.highFive(items))

