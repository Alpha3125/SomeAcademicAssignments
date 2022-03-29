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

    def printStack(self):
        print('\nTOP')
        current=self.top
        while current !=None:
            print(current.data)
            current=current.next
        print('BOTTOM')

def decToBinStack(n,obj):
    x=0
    while n!=0:
        x*=10
        x+=n%2
        n=n//2
    while x!=0:
        dig=x%10
        obj.push(dig)
        x=x//10

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
        print(x)


n=int(input('Enter a positive number: '))
if n<0:
    print('ERROR! Please enter a positve number')
else:
    Binary=Stack()
    decToBinStack(n,Binary)
    Binary.printStack()
    #k=input('ADD ONE!')
    #Binary.addOne()
    binToDec(Binary)
