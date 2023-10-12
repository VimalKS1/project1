class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None

    def push(self,n):
        if self.top==None:
            self.top=n
        else:
            n.next=self.top
            self.top=n
    def disp(self):
        temp=self.top
        while(temp.next!=None):
            print(temp.data,end="\n")
            temp=temp.next
        print(temp.data,end="\n")
    def pop(self):
        temp=self.top
        self.top=temp.next
        temp.next=None
s=stack()
n1=node(10)
n2=node(10)
n3=node(30)
n4=node(40)
s.push(n1)

s.push(n2)
s.disp()
        
