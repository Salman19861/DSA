#Circular Queue Using Singly Linked List
class Node:
    def __init__(self,key,value):
        self.key=key 
        self.value=value 
        self.next=None 
class CircularQueue:
    def __init__(self):
        self.front=None 
        self.rear=None 
    def isEmpty(self):
        if self.front==None and self.rear==None :return True
        return False 
    def checkIfNodeExist(self,node):
        temp=self.front
        exist=False 
        if temp.key==node.key:
            exist=True 
            return exist 
        temp=temp.next 
        while(temp!=self.front):
            if temp.key==node.key:
                exist=True 
                break 
            temp=temp.next 
        return exist 
    
    def enqueue(self,node):
        if self.isEmpty():
            self.front=node
            self.rear=node
            print('node pushed')
        elif self.checkIfNodeExist(node):
            print('node with same key not allowed')
        else:
            self.rear.next=node  
            self.rear=node 
            node.next=self.front
            print('node pushed')
    def count(self):
        count=0
        temp=self.front
        count+=1 
        temp=temp.next 
        while(temp!=self.front):
            count+=1 
            temp=temp.next 
        return count 
    def dequeue(self):
        if(self.isEmpty()):
            print('Queue is empty')
        else:
            if(self.front==self.rear):
                temp=self.front
                self.front=None 
                print(f"element dequeued queue is empty now")
            else:
                temp=self.front
                self.front=self.front.next
                self.rear.next=self.front 
                print('element dequeued')

    def display(self):
        if(self.isEmpty()):
            print('queue is empty')
        else:
            temp=self.front 
            print(f"({temp.key},{temp.value})",end='')
            temp=temp.next 
            while(temp!=self.front):
                print(f"({temp.key},{temp.value})",end='')
                temp=temp.next 

nodeObj=Node(1,11)
nodeObj2=Node(2,12)
nodeObj3=Node(3,13)
nodeObj4=Node(4,14)
nodeObj5=Node(5,15)

nodeObj6=Node(5,20)

myQ=CircularQueue()
myQ.enqueue(nodeObj)
myQ.enqueue(nodeObj2)
myQ.enqueue(nodeObj3)
myQ.enqueue(nodeObj4)
myQ.enqueue(nodeObj5)

myQ.enqueue(nodeObj6)

print(myQ.isEmpty())
myQ.display()
print()
myQ.dequeue()
myQ.display()
print()
print(myQ.count())
