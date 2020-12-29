


>>> import collections
>>> d=collections.OrderedDict()
>>> d['a']='A'
>>> d['b']='B'
>>> d['c']='C'
>>> d
OrderedDict([('a', 'A'), ('b', 'B'), ('c', 'C')])
>>> for k,v in d.items():
	print k,v

	
a A
b B
c C



