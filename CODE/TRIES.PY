class Node:
    def __init__(self,s):
        self.data=s
        self.child={}
        self.maxkey=None
        self.max=0
    def update_max(self,key):
        cnt=self.child[key][1]
        if self.max<cnt:
            self.maxkey=key
            self.max=cnt


class tree:
    def __init__(self,s):
        curr=Node('/')
        self.top=curr
        for words in s:
            for ch in words:
                if ch in curr.child.keys():
                    curr.child[ch][1]+=1
                    curr.update_max(ch)
                    curr=curr.child[ch][0]
                else:
                    temp=Node(ch)
                    curr.child[ch]=[temp,1]
                    curr.update_max(ch)
                    curr=temp
            curr=self.top

