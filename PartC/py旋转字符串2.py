
class Solution(object):
    def rotate(self,list2, n):
        if not list2:
            return []

        len2 = len(list2)

        def reverse(list2,i,j):
            while i<j:
                temp = list2[i]
                list2[i] = list2[j]
                list2[j] = temp
                i+=1
                j-=1

            return list2 
        
        n =n%len2
        reverse(list2, 0, n-1)
        reverse(list2,n,len(list2)-1)
        reverse(list2,0, len(list2)-1)

        return list2

if __name__  == "__main__":
    list2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
    n =4
    s = Solution()
    print(s.rotate(list2, n))

