def Calc(userInput):
    stack=[]
    for i in list(userInput):
        if i in list('0123456789'):
            stack.append(int(i))
        elif i in list('+-*/'):
            if len(stack)>1:
                if i=='+':stack.append(stack.pop()+stack.pop())
                if i=='-':stack.append(stack.pop()-stack.pop())
                if i=='*':stack.append(stack.pop()*stack.pop())
                if i=='/':stack.append(stack.pop()/stack.pop())
            
        elif i in list('#$%&'):
            print(stack)
        elif i=='^':
            print(stack.pop())
        elif i=='!':
            exit()
    print(stack)
Calc('12+34+*')


#Task 1:
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        if self.isFull(self.stack):
            print('stack overflow')
        else: 
            self.stack.append(item)
            print(f"item {item} inserted")
    
    def isEmpty(self,stack):
        if len(stack)<1:
            return True 
        else:
            return False        
    
    def Pop(self):
        if self.isEmpty(self.stack):
             print('stack underflow')
        else: 
            item=self.stack.pop()
            print(f"{item} popped ")

    def getTop(self):
        if self.isEmpty(self.stack):
             print('stack is empty')
        else:
             print(self.stack[-1])

    def isFull(self,stack):
         if len(stack)==101:
            return True 
         else:
             return False 
    def display(self):
        print(self.stack)

#Task 2 :
obj=Stack()
obj.push(1)
obj.push(7)
obj.push(5)
obj.push(2)
obj.Pop()
obj.display()
obj.push(9)
obj.display()











































# #Question 5:
# class GroceryStore:
#     checkOut1,checkOut2,checkOut3=[],[],[]
#     allCheckouts,front,rear=[checkOut1,checkOut2,checkOut3],-1,-1
    
#     def isEmpty(self):
#         if self.front==-1 and self.rear==-1:return True
#         return False 
    
#     def enqueue(self,item):
#         if self.isEmpty():
#             self.front,self.rear=0,0
#         else:
#             self.rear+=1
#         print('Welcome ',item,'!\n','We totally have 3 Checkouts:')
#         print('Your Default Checkout is = 1st Checkout ')
#         ap=int(input('Chose a Checkout : \n input\n 1 for Checkout 1\n 2 to move to Checkout 2\n'
#         ' 3 to move to Checkout 3\n'))
#         self.allCheckouts[ap-1].append(item) 

#     def display(self):
#         for i in range(len(self.allCheckouts)):
#             print(f"Checkout {i+1} Customers: {self.allCheckouts[i]}")

# obj=GroceryStore()    
# obj.enqueue('Ali')
# obj.enqueue('Xubair')
# obj.enqueue('Adil')
# obj.enqueue('Xahid')
# obj.display()





# #Question 4
# class Queue:
#     queue,front,rear=[],-1,-1
    
#     def isEmpty(self):
#         if self.front==-1 and self.rear==-1:return True
#         return False 
    
#     def enqueue(self,item):
#         if self.isEmpty():self.front,self.rear=0,0
#         else:self.rear+=1
#         self.queue.append(item) 

#     def display(self):print(self.queue)

#     def wait(self,i):
#         perHeadTakentime=20
#         haveToWait=0
#         for f in range(len(self.queue)):
#             if self.queue[f]==self.queue[i]: break  
#             haveToWait+=perHeadTakentime
#         print('Customer should wait  : ',haveToWait,' minutes before serving by a teller.')
# obj=Queue()    
# obj.enqueue(31)
# obj.enqueue(52)
# obj.enqueue(13)
# obj.enqueue(35)
# obj.wait(2)#customer at index 2 of the queue










# #Question 3
# class Queue:
#     queue,front,rear=[],-1,-1
    
#     def isEmpty(self):
#         if self.front==-1 and self.rear==-1:return True
#         return False 
    
#     def enqueue(self,item):
#         if self.isEmpty():self.front,self.rear=0,0
#         else:self.rear+=1
#         self.queue.append(item) 

#     def reverseQ(self):
#         reversed=[]
#         for i in range(len(self.queue)-1,0-1,-1):
#             reversed.append(self.queue[i])
#         self.queue=reversed

#     def display(self):print(self.queue)

#     def wait(self,i):
#         perHeadTakentime=10
#         haveToWait=0
#         for f in range(len(self.queue)):
#             if self.queue[f]==self.queue[i]: break  
#             haveToWait+=perHeadTakentime
#         print('Customer have to wait about : ',haveToWait,'minutes on hold.')
# obj=Queue()    
# obj.enqueue(1)
# obj.enqueue(2)
# obj.enqueue(3)
# obj.enqueue(5)
# print('Before reversing: ')
# obj.display()
# obj.reverseQ()
# print('After Reversing: ')
# obj.display()
# obj.wait(1)#customer at index 1 of the queue





