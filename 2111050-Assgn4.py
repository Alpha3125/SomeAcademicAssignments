class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Stack:
    def __init__(self):
        self.top=None

    def push(self,data):
        newNode=Node(data)
        if self.top==None:
            self.top=newNode
        else:
            newNode.next=self.top
            self.top=newNode
            
    def pop(self):
        if self.top!=None:
            x=self.top.data
            self.top=self.top.next
            return x
        else:
             return None

    def printStack(self):
        print('\nTOP')
        current=self.top
        while current !=None:
            print(current.data)
            current=current.next
        print('BOTTOM')
        
    def printStackFromBottom(self):
        Temp=Stack()
        while True:
            x=self.pop()
            if x==None:
                break
            else:
                Temp.push(x)
        print('\nBOTTOM')
        current=Temp.top
        while current !=None:
            print(current.data)
            current=current.next
        print('TOP')
        self=Temp
            
    def addOne(self):
        Temp=Stack()
        carry=1
        while True:
            x=self.pop()
            print(x)
            if x==None:
                print('broke')
                break
            else:
                x+=carry
                if x==2:
                    Temp.push(0)
                    carry=1
                else:
                    Temp.push(x)
        while True:
            x=Temp.pop()
            if x==None:
                break
            else:
                self.push(x)
        

def decToBinStack(n,obj):
    dig=[]
    while n!=0:
        dig.append(n%2)
        n=n//2
    for i in range(-1,-1-1*len(dig),-1):
        obj.push(dig[i])

def binToDec(obj):
    if obj.top==None:
        print('Empty')
    else:
        x,i=0,0
        current= obj.top
        while current != None:
            x=x+current.data*(2**i)
            current=current.next
            i+=1
        print('DECIMAL:',x)


n=int(input('Enter a positive number: '))
if n<0:
    print('ERROR! Please enter a positve number')
else:
    Binary=Stack()
    decToBinStack(n,Binary)
    Binary.printStack()
    Binary.printStackFromBottom()
    k=input('ADD ONE!')
    Binary.addOne()
    Binary.printStackFromBottom()
    binToDec(Binary)
