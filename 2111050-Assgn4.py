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
        current=self.top
        while current !=None:
            print(current.data)
            current=current.next
            
        
def reverse(obj1,obj2):
    while True:
        x=obj1.pop()
        if x==None:
            break
        else:
            obj2.push(x)
            
def addOne(obj1,obj2):
        carry=1
        while True:
            x=obj1.pop()
            if x==None:
                break
            else:
                x+=carry
                carry=0
                if x==2:
                    obj2.push(0)
                    carry=1
                else:
                    obj2.push(x)
        if carry==1:
            obj2.push(carry)
        
def decToBinStack(n,obj):
    while n!=0:
        obj.push(n%2)
        n=n//2
        
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
        print('\nDECIMAL:',x)


n=int(input('\nEnter a positive number: '))
if n<0:
    print('ERROR! Please enter a positve number')
else:
    Binary1=Stack()
    Binary2=Stack()
    decToBinStack(n,Binary1)
    reverse(Binary1,Binary2)
    Binary2.printStack()
    k=input('\n\t\tADD ONE\n')
    addOne(Binary2,Binary1)
    reverse(Binary1,Binary2)
    Binary2.printStack()
    binToDec(Binary2)
