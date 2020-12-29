

from typing import List, Tuple


class Solution():
	def destCity(self,paths:List[List[str]])->str:

		setA = set([path[0] for path in paths])
		setB = set([path[1] for path in paths])

		res =setB - setA

		res = list(res)[0]
