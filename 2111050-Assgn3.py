from types import NoneType
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            currentNode=self.head
            previousNode=None
            while type(currentNode) != NoneType :
                if data>currentNode.data:
                    previousNode = currentNode
                    currentNode=currentNode.next
                else:
                    break
            if (type(previousNode)== NoneType):
                temp=Node(data)
                temp.next=self.head
                self.head=temp
            else:
                previousNode.next=Node(data)
                previousNode.next.next=currentNode

    def display(self):
        print('HEAD', end='-->>>  ')
        currentNode=self.head
        while type(currentNode) != NoneType:
            print(currentNode.data, end='->')
            currentNode=currentNode.next
        print('>>  TAIL')

    def spellcheck(self,target):
        diary={}
        flag=0
        current=self.head
        while type(current) != NoneType :
            word=current.data
            if(word == target):
                print('WORD EXISTS')
                flag=1
                break
            else:
                dist=5
                for i in range(5):
                    if word[i]==target[i]:
                        dist-=1
                diary[word]=dist
            current=current.next
        if(flag ==0):
            for x in diary:
                min=x
                break
            for x in diary:
                if diary[x]<diary[min]:
                    min=x
            print('CLOSEST STRING: ', min)
            print('HAMMING DISTANCE: ', diary[min])

                
	

Dictionary1=LinkedList()
print('\t\t\t LEXICOGRAPHIC ORDER')
n=int(input('No. of words: '))
for i in range(n):
    data= input('Enter data item: ')
    for ch in data:
        if ch.isalpha() != True:
            print('!INCORRECT INPUT!  USE ONLY ALPHABETS')
            exit()
    Dictionary1.append(data)
print('Dictionary:   ',end=' ')
Dictionary1.display()
print('\n\n\t\t\t SPELL CHECKER')
Dictionary2=LinkedList()
n=int(input('No. of words: '))
for i in range(n):
    data= input('Enter data item: ')
    if(len(data)!=5):
        print('!INCORRECT LENGTH! MUST BE 5')
        exit()
    for ch in data:
        if ch.isalpha() != True:
            print('!INCORRECT INPUT!  USE ONLY ALPHABETS')
            exit()
    Dictionary2.append(data)
target=input('Enter Target String: ')
if(len(target)!=5):
    print('!INCORRECT LENGTH! MUST BE 5')
    exit()
Dictionary2.spellcheck(target)