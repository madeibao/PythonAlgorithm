



def typeof(variate):
  type=None
  if isinstance(variate,int):
      type = "int"
  elif isinstance(variate,str):
      type = "str"
  elif isinstance(variate,float):
      type = "float"
  elif isinstance(variate,list):
      type = "list"
  elif isinstance(variate,tuple):
      type = "tuple"
  elif isinstance(variate,dict):
      type = "dict"
  elif isinstance(variate,set):
      type = "set"
  return type


list2 = [1, 23, 3, 4, 3, 3, 434,]
print(typeof(list2))
