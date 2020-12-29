

>>> s = 'hello good boy doiido'
>>> print s.startswith('h')
True
>>> print s.startswith('hel')
True
>>> print s.startswith('h',4)
False
>>> print s.startswith('go',6,8)
True
 
#匹配空字符集
>>> print s.startswith('')
True
#匹配元组
>>> print s.startswith(('t','b','h'))
True




