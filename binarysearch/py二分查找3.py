

class Solution(object):
	def find(self,arrs, target):

		i,j = 0, len(arrs)-1
		while i<j:
			mid = (i+j)//2
			if arrs[mid] == target:
				return mid
			elif arrs[mid]>target:
				j = mid-1
			else:
				i = mid+1
		return -1



if __name__ == "__main__":
	s =Solution()
	list2 =[1,2,3,4,5,6,7,8,9,10]
	target = 5
	print(s.find(list2, target))

	
