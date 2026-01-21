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
    def pred(self,k):
        ans=""
        curr=self.top
        for i in k:
            
            if i not in curr.child.keys():
                print("given combination not found")
                return (None)
            else:
                curr=curr.child[i][0]
                ans=ans+i
        while curr.child.keys():
            ch=curr.maxkey
            ans=ans+ch
            curr=curr.child[ch][0]
        return (ans)
            
