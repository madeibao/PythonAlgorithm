
'''
遇到问题没人解答？小编创建了一个Python学习交流QQ群：579817333 
寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！
'''
import sys

class ostream:
    def __init__(self, file):
        self.file = file
        
    def __lshift__(self, obj):
        self.file.write(str(obj));
        return self

cout = ostream(sys.stdout)
cerr = ostream(sys.stderr)
nl = '\n'

x = 2
y = 3

cout << x << " " << y << nl




