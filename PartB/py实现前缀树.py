



class Trie:
    def __init__(self):

        # 首先建立一个字典。
        self.dic={}

    def insert(self,strr):
        a=self.dic
        for i in strr:
            if not i in a:
                a[i]={}
            a=a[i]
        a["end"]=True

    def search(self,strr):
        a=self.dic
        for i in strr:
            if not i in a:
                return False
            a=a[i]
        if "end" in a:
            return True
        else:
            return False
    def startsWith(self,strr):
        a=self.dic
        for i in strr:
            if not i in a:
                return False
            a=a[i]
        return True



if __name__ == "__main__":
    s =Trie()
    s.insert("apple")
    print(s.search("apple"))


