# # def push(stack,item):
# #     stack.append(item)
# # def pop(stack):
# #     if empty(stack):
# #         return 'stack underflow'
# #     stack.pop()
# #     return 'popped'
# # def empty(stack):
# #     if not stack:
# #         return True
# #     return False 
# # stack=[]
# # push(stack,12)
# # push(stack,13)
# # push(stack,14)
# # print(stack)
# # pop(stack)
# # empty(stack)
# # print(stack)



# # #python mai list as a dynamic array kam krta hai isssliy no need of isFull method lekin phir bhi hm
# # #nei 5 max items condisr ikiye hai iss example mei.
# # class Stack:
# #     stack,top=[0,0,0,0,0],-1 
# #     def isEmpty(self):
# #         if self.top==-1:
# #             return True
# #         return False 
# #     def isFull(self):
# #         if self.top==4:
# #             return True 
# #         return False #in python ...
# #     def push(self,item):
# #         if (self.isFull()):
# #             print( 'stack overflow')
# #         else:
# #             self.top+=1
# #             self.stack[self.top]=item #or 
# #             return True
# #     def pop(self):
# #         if self.isEmpty():
# #             print('stack underflow ')
# #         else:
# #             self.stack[self.top]=0 
# #             self.top-=1
# #             return 0 
# #     def count(self):
# #         print(f"total items: {self.top+1}")
# #     def peek(self,index):
# #         if self.isEmpty():
# #             print('stack underflow')
# #         print(f"item at index {index} is: {self.stack[index]} ")

# #     def change(self,index,item):
# #         if self.stack[index]:
# #             self.stack[index]=item 
# #             return self.stack[index]
# #         print( f"index: {index} doesn't exist in stack")
# #     def display(self):
# #         print(self.stack[::-1])

# # obj=Stack()
# # obj.push(12)
# # obj.display()
# # obj.push(3)
# # obj.push(44)
# # obj.push(55)
# # obj.push(67)
# # obj.push(45) #stack overflw
# # obj.display()
# # obj.change(3,100)
# # obj.display()
# # print(obj.isFull())
# # print(obj.isEmpty())
# # obj.count()
# # obj.pop()
# # obj.count()
# # obj.peek(1)
# # obj.display()  #bcause of pop()






# # # while(True):
# # #     print('''Select an Optoin:
# # #     0.Exit
# # #     1.push
# # #     2.pop
# # #     3.isEmpty
# # #     4.isFull
# # #     5.peek
# # #     6.count
# # #     7.change
# # #     8.display
# # #     9.clear command prompt''')
# # #     a=int(input())
# # #     if a==1:
# # #         item=input('enter item to push to stack: ')
# # #         obj.push(item)
# # #         break
# # #     if a==2:
# # #         obj.pop()
# # #     if a==3:
# # #         if obj.isEmpty():print('stack is empty')
# # #         else:print('stack is not empty')
# # #     if a==4:
# # #         if obj.isFull():print('stack is full')
# # #         else:print('stack is not full')
# # #     if a==5:
# # #         input=int(input('enter index to peek: '))
# # #         obj.peek(input)
# # #     if a==6:obj.count()
# # #     if a==7:
# # #         print(obj.stack)
# # #         index=int(input('enter index:'))
# # #         item=input('enter item: ')
# # #         obj.change(index,item)
# # #     if a==8:obj.display()
# # #     if a==9:system('cls')
# # #     else:break



# # def isEmpty(queue):
# #     if not queue: return True
# #     return False 
# # def enqueue(queue,item):queue.append(item)
# # def dequeue(queue):
# #     if isEmpty(queue):
# #         print('queue is empty')
# #     else:
# #         p=queue.pop(0)
# #         print(p)

# # queue=[]
# # enqueue(queue,2)
# # enqueue(queue,3)
# # enqueue(queue,6)
# # enqueue(queue,4)
# # print(queue)
# # dequeue(queue)
# # dequeue(queue)

# # print(queue)









# # #here we are handling index through front and rear vars rather than using a python feature. 
# # from os import system


# # class Queue:
# #     queue,front,rear=[],-1,-1
    
# #     def isEmpty(self):
# #         if self.front==-1 and self.rear==-1:return True
# #         return False 
    
# #     def enqueue(self,item):
# #         if self.isEmpty():self.front,self.rear=0,0
# #         else:self.rear+=1
# #         self.queue.append(item) 

# #     def dequeue(self):
# #         if self.isEmpty():print('queue is already empty')
# #         elif self.rear==self.front:
# #             value=self.queue.pop(0)
# #             self.rear=-1
# #             self.front=-1
# #             return value 
# #         else:
# #             value=self.queue.pop(0)
# #             self.front+=1
# #             return value 
    
# #     def count(self):print(f"total items in queue: {self.rear-self.front+1}")#ye bydefault 1 dikhaega our baqi apna kam 
# #     def display(self):print(self.queue)                                         #shi krega.
# #     def clearterminal(self):system('cls')

# # obj=Queue()    
# # choice=None
# # while choice!=0:
# #     print('''
# # 1.enqueue
# # 2.dequeue
# # 3.isEmpty
# # 4.count
# # 5.display
# # 6.clear terminal
# #     ''')
# #     choice=int(input('enter ur choice: '))
# #     if choice==1:
# #         item=input('enter item to enqueue: ')
# #         obj.enqueue(item)
# #     elif choice==2:obj.dequeue()
# #     elif choice==3:print(obj.isEmpty())
# #     elif choice==4:obj.count()
# #     elif choice==5:obj.display()
# #     elif choice==6:obj.clearterminal()

# # Circular Queue implementation in Python


# class MyCircularQueue():
#     def __init__(self, k):
#         self.k = k
#         self.queue = [None] * k
#         self.head = self.tail = -1

#     # Insert an element into the circular queue
#     def enqueue(self, data):
#         if ((self.tail + 1) % self.k == self.head):
#             print("The circular queue is full\n")

#         elif (self.head == -1):
#             self.head = 0
#             self.tail = 0
#             self.queue[self.tail] = data
#         else:
#             self.tail = (self.tail + 1) % self.k
#             self.queue[self.tail] = data

#     # Delete an element from the circular queue
#     def dequeue(self):
#         if (self.head == -1):
#             print("The circular queue is empty\n")

#         elif (self.head == self.tail):
#             temp = self.queue[self.head]
#             self.head = -1
#             self.tail = -1
#             return temp
#         else:
#             temp = self.queue[self.head]
#             self.head = (self.head + 1) % self.k
#             return temp

#     def printCQueue(self):
#         if(self.head == -1):
#             print("No element in the circular queue")

#         elif (self.tail >= self.head):
#             for i in range(self.head, self.tail + 1):
#                 print(self.queue[i], end=" ")
#             print()
#         else:
#             for i in range(self.head, self.k):
#                 print(self.queue[i], end=" ")
#             for i in range(0, self.tail + 1):
#                 print(self.queue[i], end=" ")
#             print()


# # Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(5)
# obj.enqueue(1)
# obj.enqueue(2)
# obj.enqueue(3)
# obj.enqueue(4)
# obj.enqueue(5)
# print("Initial queue")
# obj.printCQueue()

# obj.dequeue()
# print("After removing an element from the queue")
# obj.printCQueue()





# # This is the CircularQueue class
# class CircularQueue:
#   # constructor for the class
#   # taking input for the size of the Circular queue 
#   # from user
#   def __init__(self, maxSize):
#     self.queue = list()
#     # user input value for maxSize
#     self.maxSize = maxSize
#     self.head = 0
#     self.tail = 0

#   # add element to the queue
#   def enqueue(self, data):
#     # if queue is full
#     if self.size() == (self.maxSize - 1):
#       return("Queue is full!")
#     else:
#       # add element to the queue
#       self.queue.append(data)
#       # increment the tail pointer
#       self.tail = (self.tail+1) % self.maxSize
#       return True
  
#   # remove element from the queue
#   def dequeue(self):
#     # if queue is empty
#     if self.size() == 0:
#       return("Queue is empty!")
#     else:
#       # fetch data
#       data = self.queue[self.head]
#       # increment head
#       self.head = (self.head+1) % self.maxSize
#       return data
  
#   # find the size of the queue
#   def size(self):
#     if self.tail >= self.head:
#       qSize = self.tail - self.head
#     else:
#       qSize = self.maxSize - (self.head - self.tail)
#     # return the size of the queue
#     return qSize

# # input 7 for the size or anything else
# size = input("Enter the size of the Circular Queue")
# q = CircularQueue(int(size)+1)

# # change the enqueue and dequeue statements as you want
# print(q.enqueue(10))
# print(q.enqueue(20))
# print(q.dequeue())
# print(q.size())








#Linked List
# class Node:
#     def __init__(self,data=None):
#         self.data=data 
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
        
#     def display(self):
#         disp=[]
#         cur=self.head
#         disp.append(cur.data)
#         while cur.next!=None:
#             cur=cur.next
#             disp.append(cur.data)
#         print(disp)

     
# obj=LinkedList()
# obj.head=Node(10)
# element2=Node(20)
# element3=Node(30)
# obj.head.next=element2
# element2.next=element3

# obj.display()




# class Node:
#     def __init__(self,data=None):
#         self.data=data 
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=Node()

#     def insertData(self,data):
#         newNode=Node(data)
#         cur=self.head 
#         while cur.next!=None:
#             cur=cur.next
#         cur.next=newNode

#     def display(self):
#         disp=[]
#         cur=self.head
#         while cur.next!=None:
#             cur=cur.next
#             disp.append(cur.data)
#         print(disp)

# obj=LinkedList()
# obj.insertData(10)
# obj.insertData(20)
# obj.insertData(30)

# obj.display()


# # Linked list implementation in Python
# class Node:
#     # Creating a node
#     def __init__(self, item):
#         self.item = item
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None

        
# if __name__ == '__main__':
#     linked_list = LinkedList()
#     # Assign item values
#     linked_list.head = Node(1)
#     second = Node(2)
#     third = Node(3)
#     # Connect nodes
#     linked_list.head.next = second
#     second.next = third
#     # Print the linked list item
#     while linked_list.head != None:
#         print(f"{linked_list.head.item}", end=" ")
#         linked_list.head = linked_list.head.next


#Singly linked list all operations:
# Linked list operations in Python
# # Create a node
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:

#     def __init__(self):
#         self.head = None

#     # Insert at the beginning
#     def insertAtBeginning(self, new_data):
#         new_node = Node(new_data)

#         new_node.next = self.head
#         self.head = new_node

#     # Insert after a node
#     def insertAfter(self, prev_node, new_data):

#         if prev_node is None:
#             print("The given previous node must inLinkedList.")
#             return

#         new_node = Node(new_data)
#         new_node.next = prev_node.next
#         prev_node.next = new_node

#     # Insert at the end
#     def insertAtEnd(self, new_data):
#         new_node = Node(new_data)

#         if self.head is None:
#             self.head = new_node
#             return

#         last = self.head
#         while (last.next):
#             last = last.next

#         last.next = new_node

#     # Deleting a node
#     def deleteNode(self, position):

#         if self.head is None:
#             return

#         temp = self.head

#         if position == 0:
#             self.head = temp.next
#             temp = None
#             return

#         # Find the key to be deleted
#         for i in range(position - 1):
#             temp = temp.next
#             if temp is None:
#                 break

#         # If the key is not present
#         if temp is None:
#             return

#         if temp.next is None:
#             return

#         next = temp.next.next

#         temp.next = None

#         temp.next = next

#     # Search an element
#     def search(self, key):

#         current = self.head

#         while current is not None:
#             if current.data == key:
#                 return True

#             current = current.next

#         return False

#     # Sort the linked list
#     def sortLinkedList(self, head):
#         current = head
#         index = Node(None)

#         if head is None:
#             return
#         else:
#             while current is not None:
#                 # index points to the node next to current
#                 index = current.next

#                 while index is not None:
#                     if current.data > index.data:
#                         current.data, index.data = index.data, current.data

#                     index = index.next
#                 current = current.next

#     # Print the linked list
#     def printList(self):
#         temp = self.head
#         while (temp):
#             print(str(temp.data) + "---> ", end="")
#             temp = temp.next


# if __name__ == '__main__':

#     llist = LinkedList()
#     llist.insertAtEnd(1)
#     llist.insertAtBeginning(2)
#     llist.insertAtBeginning(3)
#     llist.insertAtEnd(4)
#     llist.insertAfter(llist.head.next, 5)

#     print('linked list:')
#     llist.printList()

#     print("\nAfter deleting an element:")
#     llist.deleteNode(3)
#     llist.printList()

#     print()
#     item_to_find = 3
#     if llist.search(item_to_find):
#         print(str(item_to_find) + " is found")
#     else:
#         print(str(item_to_find) + " is not found")

#     llist.sortLinkedList(llist.head)
#     print("Sorted List: ")
#     llist.printList()










# Note: In the case of the head node, prev points to null, and in the case of the tail pointer, next points to null. 
# Here, one is a head node and three is a tail node.

import gc

# node creation

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    # insert node at the front
    def insert_front(self, data):

        # allocate memory for newNode and assign data to newNode
        new_node = Node(data)

        # make newNode as a head
        new_node.next = self.head

        # assign null to prev (prev is already none in the constructore)

        # previous of head (now head is the second node) is newNode
        if self.head is not None:
            self.head.prev = new_node

        # head points to newNode
        self.head = new_node

    # insert a node after a specific node
    def insert_after(self, prev_node, data):

        # check if previous node is null
        if prev_node is None:
            print("previous node cannot be null")
            return

        # allocate memory for newNode and assign data to newNode
        new_node = Node(data)

        # set next of newNode to next of prev node
        new_node.next = prev_node.next

        # set next of prev node to newNode
        prev_node.next = new_node

        # set prev of newNode to the previous node
        new_node.prev = prev_node

        # set prev of newNode's next to newNode
        if new_node.next:
            new_node.next.prev = new_node

    # insert a newNode at the end of the list
    def insert_end(self, data):

        # allocate memory for newNode and assign data to newNode
        new_node = Node(data)

        # assign null to next of newNode (already done in constructor)

        # if the linked list is empty, make the newNode as head node
        if self.head is None:
            self.head = new_node
            return

        # store the head node temporarily (for later use)
        temp = self.head

        # if the linked list is not empty, traverse to the end of the linked list
        while temp.next:
            temp = temp.next

        # now, the last node of the linked list is temp

        # assign next of the last node (temp) to newNode
        temp.next = new_node

        # assign prev of newNode to temp
        new_node.prev = temp

        return

    # delete a node from the doubly linked list
    def deleteNode(self, dele):

        # if head or del is null, deletion is not possible
        if self.head is None or dele is None:
            return

        # if del_node is the head node, point the head pointer to the next of del_node
        if self.head == dele:
            self.head = dele.next

        # if del_node is not at the last node, point the prev of node next to del_node to the previous of del_node
        if dele.next is not None:
            dele.next.prev = dele.prev

        # if del_node is not the first node, point the next of the previous node to the next node of del_node
        if dele.prev is not None:
            dele.prev.next = dele.next

        # free the memory of del_node
        gc.collect()

    # print the doubly linked list
    def display_list(self, node):

        while node:
            print(node.data, end="->")
            last = node
            node = node.next


# initialize an empty node
d_linked_list = DoublyLinkedList()

d_linked_list.insert_end(5)
d_linked_list.insert_front(1)
d_linked_list.insert_front(6)
d_linked_list.insert_end(9)

# insert 11 after head
d_linked_list.insert_after(d_linked_list.head, 11)

# insert 15 after the seond node
d_linked_list.insert_after(d_linked_list.head.next, 15)

d_linked_list.display_list(d_linked_list.head)

# delete the last node
d_linked_list.deleteNode(d_linked_list.head.next.next.next.next.next)

print()
d_linked_list.display_list(d_linked_list.head)



# Python code to perform circular linked list operations
# Note: We will be using the singly circular linked list to represent the working of circular linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    def addToEmpty(self, data):

        if self.last != None:
            return self.last

        # allocate memory to the new node and add data to the node
        newNode = Node(data)

        # assign last to newNode
        self.last = newNode

        # create link to iteself
        self.last.next = self.last
        return self.last

    # add node to the front
    def addFront(self, data):

        # check if the list is empty
        if self.last == None:
            return self.addToEmpty(data)

        # allocate memory to the new node and add data to the node
        newNode = Node(data)

        # store the address of the current first node in the newNode
        newNode.next = self.last.next

        # make newNode as last
        self.last.next = newNode

        return self.last

    # add node to the end
    def addEnd(self, data):
        # check if the node is empty
        if self.last == None:
            return self.addToEmpty(data)

        # allocate memory to the new node and add data to the node
        newNode = Node(data)

        # store the address of the last node to next of newNode
        newNode.next = self.last.next

        # point the current last node to the newNode
        self.last.next = newNode

        # make newNode as the last node
        self.last = newNode

        return self.last

    # insert node after a specific node
    def addAfter(self, data, item):

        # check if the list is empty
        if self.last == None:
            return None

        newNode = Node(data)
        p = self.last.next
        while p:

            # if the item is found, place newNode after it
            if p.data == item:

                # make the next of the current node as the next of newNode
                newNode.next = p.next

                # put newNode to the next of p
                p.next = newNode

                if p == self.last:
                    self.last = newNode
                    return self.last
                else:
                    return self.last
            p = p.next
            if p == self.last.next:
                print(item, "The given node is not present in the list")
                break

    # delete a node
    def deleteNode(self, last, key):

        # If linked list is empty
        if last == None:
            return

        # If the list contains only a single node
        if (last).data == key and (last).next == last:

            last = None

        temp = last
        d = None

        # if last node is to be deleted
        if (last).data == key:

            # find the node before the last node
            while temp.next != last:
                temp = temp.next

            # point temp node to the next of last i.e. first node
            temp.next = (last).next
            last = temp.next

        # travel to the node to be deleted
        while temp.next != last and temp.next.data != key:
            temp = temp.next

        # if node to be deleted was found
        if temp.next.data == key:
            d = temp.next
            temp.next = d.next

        return last

    def traverse(self):
        if self.last == None:
            print("The list is empty")
            return

        newNode = self.last.next
        while newNode:
            print(newNode.data, end=" ")
            newNode = newNode.next
            if newNode == self.last.next:
                break


# Driver Code
if __name__ == "__main__":

    cll = CircularLinkedList()

    last = cll.addToEmpty(6)
    last = cll.addEnd(8)
    last = cll.addFront(2)
    last = cll.addAfter(10, 2)

    cll.traverse()

    last = cll.deleteNode(last, 8)
    print()
    cll.traverse()









def linearSearch(ls,target):
    for i in range(len(ls)):
        if ls[i]==target:return (f"target found: --> {ls[i]}")
    return('target doesnt exist')
print(linearSearch([1,2,3,4,5,10],2))











def binarySearch(ls,left,right,x):
    while(left<=right):
        mid=left+(right-left)//2
        if(ls[mid]==x):return mid 
        elif(ls[mid]<x):left=mid+1
        else:right=mid-1
    return -1
ls=[1,2,3,4,5,6,7]
target=6
obj=binarySearch(ls,0,len(ls)-1,target)
if(obj)!=-1:print(f"x= {ls[obj]} found at index {obj}")
else: print('x not found')




def selectionSort(ls,size):
    for i in range(size):
        min=i
        for j in range(i+1,size):
            if ls[j]<ls[min]:
                min=j
        ls[i],ls[min]=ls[min],ls[i]
ls=[23,2,1,5,8]
selectionSort(ls,len(ls))
print(ls)



def insertionSort(ls,size):
    for i in range(1,size):
        key=ls[i]
        j=i-1
        while((j>=0) and (ls[j]>key)):
            ls[j+1]=ls[j]
            j=j-1
        ls[j+1]=key
ls=[9,7,3,6,2]
insertionSort(ls,len(ls))
print(ls)













def bubbleSort(ls):
    for i in range(len(ls)):
        for j in range(len(ls)-i-1):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]

ls=[9,7,3,6,2]
bubbleSort(ls)
print(ls)



def optimizeBubbleSort(ls):
    rounds=0
    for i in range(len(ls)):
        rounds+=1
        flag=False
        for j in range(len(ls)-i-1):
            if ls[j]>ls[j+1]:
                flag=True
                ls[j],ls[j+1]=ls[j+1],ls[j]
        if flag==False: break
    print(rounds)

ls=[5,2,4,3,6]
optimizeBubbleSort(ls)
print(ls)



def sum(n):
    result=0
    for i in range(n+1):
        result+=i 
    print(result)
sum(32131111)

def sum2(nmbr):
    res=(nmbr*(nmbr+1))//2
    print(res)
sum2(32131111)



# MergeSort in Python


def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)





# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)






# Counting sort in Python programming


def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)




# Radix sort in Python


# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


data = [121, 432, 564, 23, 1, 45, 788]
radixSort(data)
print(data)




# Shell sort in python


def shellSort(array, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


data = [9, 8, 3, 7, 5, 6, 4, 1]
size = len(data)
shellSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)


# #INFIX TO POSTFIX:
def presedence(operator):
    if operator=='+' or operator=='-':
        return 1
    elif operator=='*' or operator=='/':
        return 2
    elif operator=='^':
        return 3
    return -1


def infixToPostfix(stack,infixExpression):
    postfix=''
    for i in range(len(infixExpression)):
        if infixExpression[i]>='a'  and infixExpression[i]<='z' or infixExpression[i]>='A'  and infixExpression[i]<='Z':
            postfix+=infixExpression[i]

        elif infixExpression[i]=='(':
            stack.append(infixExpression[i])
        
        elif infixExpression[i]==')':
            while(len(stack)>0):
                if stack[-1]=='(':
                    stack.pop()
                    break
                else:postfix+=stack.pop()
        
        elif infixExpression[i] in list('+-*/^'):
            if len(stack)==0: 
                stack.append(infixExpression[i])
            
            else:
                if presedence(infixExpression[i])>presedence(stack[-1]):
                    stack.append(infixExpression[i])

                elif presedence(infixExpression[i])==presedence(stack[-1]) and infixExpression[i]=='^':
                    stack.append(infixExpression[i])

                else:
                    while((len(stack)>0) and (presedence(infixExpression[i])<=(presedence(stack[-1])))):
                        postfix+=stack.pop()
                    stack.append(infixExpression[i])
        
    while(len(stack)>0):
        postfix+=stack.pop()

    print(postfix)        
# infixExpression=list('((a+b-c)*d^e^f)/g')
infixExpression=list('(A+B^C)*D+E')
stack=[]
infixToPostfix(stack,infixExpression) #Output should be: 'ab+c-def^^*g/








#INFIX TO PREFIX:
def presedence(operator):
    if operator=='+' or operator=='-':
        return 1
    elif operator=='*' or operator=='/':
        return 2
    elif operator=='^':
        return 3
    return -1  
def replace(expression):
    ret=''
    for i in expression:
        if i=='(':
            i=')'
        elif i==')':
            i='('
        ret+=i
    return ret 
def reverse(exp):
    ret=''
    for i in range(len(exp),0,-1):
        ret+=exp[i-1]
    return ret


def infixToPrefix(stack,infixExpression):
    prefix=''
    infixExpression=replace(infixExpression)
    for i in range(len(infixExpression),0,-1):
        if infixExpression[i-1]>='a'  and infixExpression[i-1]<='z' or infixExpression[i-1]>='A'  and infixExpression[i-1]<='Z':
            prefix+=infixExpression[i-1]

        elif infixExpression[i-1]=='(':
            stack.append(infixExpression[i-1])
        
        elif infixExpression[i-1]==')':
            while(len(stack)>0):
                if stack[-1]=='(':
                    stack.pop()
                    break
                else:prefix+=stack.pop()
        
        elif infixExpression[i-1] in list('+-*/^'):
            if len(stack)==0: 
                stack.append(infixExpression[i-1])
            
            else:
                if presedence(infixExpression[i-1])>presedence(stack[-1]):
                    stack.append(infixExpression[i-1])

                elif presedence(infixExpression[i-1])==(presedence(stack[-1])) and (infixExpression[i-1]=='^'):
                    while(presedence(infixExpression[i-1])==(presedence(stack[-1])) and (infixExpression[i-1]=='^')):
                        prefix+=stack.pop()
                    stack.append(infixExpression[i-1])
                
                elif presedence(infixExpression[i-1])==presedence(stack[-1]):
                    stack.append(infixExpression[i-1])

                else:
                    while((len(stack)>0) and (presedence(infixExpression[i-1])<(presedence(stack[-1])))):
                        prefix+=stack.pop()
                    stack.append(infixExpression[i-1])
    
    while(len(stack)>0):
        prefix+=stack.pop()
    finalPrefixExpression=reverse(prefix)
    print(finalPrefixExpression)        
infixExpression=list('((a+b-c)*d^e^f)/g')
stack=[]
infixToPrefix(stack,infixExpression) #Output should be: '/*-+abc^d^efg'






def postfixToInfix(pExp):
    stack=[]
    for i in range(len(pExp)):
        if pExp[i]>='a'  and pExp[i]<='z' or pExp[i]>='A'  and pExp[i]<='Z':
            stack.append(pExp[i])
        else:
            if pExp[i] in list('+-*/^'):
                a=stack.pop()
                b=stack.pop()
                exp='('+b+pExp[i]+a+')'
                stack.append(exp)
    print(stack[-1])

postfixToInfix('ab+c-def^^*g/')
# postfixToInfix('abc*+')#a+b*c



def pretfixToInfix(pExp):
    stack=[]
    for i in range(len(pExp),0,-1):
        if pExp[i-1]>='a'  and pExp[i-1]<='z' or pExp[i-1]>='A'  and pExp[i-1]<='Z':
            stack.append(pExp[i-1])
        else:
            if pExp[i-1] in list('+-*/^'):
                a=stack.pop()
                b=stack.pop()
                exp='('+a+pExp[i-1]+b+')'
                stack.append(exp)
    print(stack[-1])

pretfixToInfix('/*-+abc^d^efg')
pretfixToInfix('+*abc')#a*b+c





def postfixToPrefix(pExp):
    stack=[]
    for i in range(len(pExp)):
        if pExp[i]>='a'  and pExp[i]<='z' or pExp[i]>='A'  and pExp[i]<='Z':
            stack.append(pExp[i])
        else:
            if pExp[i] in list('+-*/^'):
                a=stack.pop()
                b=stack.pop()
                exp=pExp[i]+b+a
                stack.append(exp)
    print(stack[-1])

postfixToPrefix('ab+c-def^^*g/')


def prefixToPostfix(pExp):
    stack=[]
    for i in range(len(pExp),0,-1):
        if pExp[i-1]>='a'  and pExp[i-1]<='z' or pExp[i-1]>='A'  and pExp[i-1]<='Z':
            stack.append(pExp[i-1])
        else:
            if pExp[i-1] in list('+-*/^'):
                a=stack.pop()
                b=stack.pop()
                exp=a+b+pExp[i-1]
                stack.append(exp)
    print(stack[-1])

prefixToPostfix('/*-+abc^d^efg')



#Stack Using Singly Linked List
class Node:
    def __init__(self,key,value):
        self.key=key 
        self.value=value 
        self.next=None 
class Stack:
    def __init__(self):
        self.top=None 
    def isEmpty(self):
        if self.top==None:return True
        return False 
    def checkIfNodeExist(self,node):
        temp=self.top 
        exist=False 
        while(temp!=None):
            if temp.key==node.key:
                exist=True 
                break 
            temp=temp.next 
        return exist 
    
    def push(self,node):
        if self.top==None:
            self.top=node
            print('node pushed')
        elif self.checkIfNodeExist(node):
            print('node with same key not allowed')
        else:
            temp=self.top 
            self.top=node 
            node.next=temp 
            print('node pushed')
    def count(self):
        count=0
        temp=self.top 
        while(temp!=None):
            count+=1 
            temp=temp.next 
        return count 
    def pop(self):
        if(self.isEmpty()):
            print('stack underflow')
        else:
            self.top=self.top.next 
            print('top element popped') 
    def peek(self):
        if(self.isEmpty()):
            print('stack underflow')
        else:
            print(f"\n({self.top.key},{self.top.value})")
             
    def display(self):
        temp=self.top 
        while(temp!=None):
            print(f"({temp.key},{temp.value})-->",end='')
            temp=temp.next 

nodeObj=Node(1,11)
nodeObj2=Node(2,12)
nodeObj3=Node(3,13)
nodeObj4=Node(4,14)
nodeObj5=Node(5,15)

nodeObj6=Node(5,20)

myStack=Stack()
myStack.push(nodeObj)
myStack.push(nodeObj2)
myStack.push(nodeObj3)
myStack.push(nodeObj4)
myStack.push(nodeObj5)

myStack.push(nodeObj6)

print(myStack.isEmpty())
myStack.display()
print()
myStack.pop()
myStack.display()
print()
print(myStack.count())
myStack.peek()
        




#Queue Using Singly Linked List
class Node:
    def __init__(self,key,value):
        self.key=key 
        self.value=value 
        self.next=None 
class Queue:
    def __init__(self):
        self.front=None 
        self.rear=None 
    def isEmpty(self):
        if self.front==None and self.rear==None :return True
        return False 
    def checkIfNodeExist(self,node):
        temp=self.front
        exist=False 
        while(temp!=None):
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
            print('node pushed')
    def count(self):
        count=0
        temp=self.front
        while(temp!=None):
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
                print('element dequeued')

    def display(self):
        if(self.isEmpty()):
            print('queue is empty')
        else:
            temp=self.front 
            while(temp!=None):
                print(f"({temp.key},{temp.value})",end='')
                temp=temp.next 

nodeObj=Node(1,11)
nodeObj2=Node(2,12)
nodeObj3=Node(3,13)
nodeObj4=Node(4,14)
nodeObj5=Node(5,15)

nodeObj6=Node(5,20)

myQ=Queue()
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







# Binary Tree or BST and AVL Tree

class TreeNode:
    def __init__(self,value=0):
        self.value=value 
        self.left=None 
        self.right=None 
class BST:
    def __init__(self):
        self.root=None
    def isEmpty(self):
        if self.root==None:return True 
        return False 

    def insertNode(self,node):
        if self.root==None:
            self.root=node
            print('node inserted as root node') 
        else:
            temp=self.root
            while(temp!=None):
                if node.value==temp.value:
                    print('no duplicate values allowed')
                    break
                elif(node.value<temp.value) and (temp.left==None):
                    temp.left=node 
                    print('node inserted at left')
                    break 
                elif(node.value<temp.value):
                    temp=temp.left 
                elif(node.value>temp.value) and (temp.right==None):
                    temp.right=node 
                    print('node inserted right')
                    break 
                else:
                    temp=temp.right 
    def insertNodeRecursively(self,rootNode,node):
        if rootNode==None:
            rootNode=node
            return rootNode
        if node.value<rootNode.value:
            rootNode.left=self.insertNodeRecursively(rootNode.left,node)
        elif node.value>rootNode.value:
            rootNode.right=self.insertNodeRecursively(rootNode.right,node)
        else:
            print('a node with same value already exist')
            return rootNode
        return rootNode #this is when we go back the original addresses will be restored to the nodes from 
        #where recursion f(x)s were called or when recursion is going to be completed or when recursion is 
        # is going to continue back upward to its parent called f(x)  where it was paused .means during backtracking. 


    def print2d(self,rootNode,space):
        globalSpace=8
        if rootNode==None:
            return 
        else:
            space+=globalSpace 
            self.print2d(rootNode.right,space)
            # print()
            for i in range(space):
                print(' ',end='')
            print(rootNode.value,'\n')
            self.print2d(rootNode.left,space)
    def printPreOrder(self,rootNode):
        if rootNode==None:return 
        print(rootNode.value,end=' ')
        self.printPreOrder(rootNode.left)
        self.printPreOrder(rootNode.right)
    def printInOrder(self,rootNode):
        if rootNode==None:return 
        self.printInOrder(rootNode.left)
        print(rootNode.value,end=' ')
        self.printInOrder(rootNode.right)
    def printPostOrder(self,rootNode):
        if rootNode==None:return 
        self.printPostOrder(rootNode.left)
        self.printPostOrder(rootNode.right)
        print(rootNode.value,end=' ')

    def iterativeSearch(self,value):
        if self.root==None:return f"value: {value} is not available in the tree"
        temp=self.root
        while(temp!=None):
            if value==temp.value:return f"value found: {temp.value}"
            elif value<temp.value:temp=temp.left
            else:temp=temp.right
        return f'value: {value} is not available in the tree'

    def height(self,rootNode):
        if rootNode==None:return -1
        else: 
            lheight=self.height(rootNode.left)
            rheight=self.height(rootNode.right)
            if lheight>rheight:
                return lheight+1
            return rheight+1 

    def printGivenLevel(self,node,level):
        if node==None:return 
        elif level==0:print(node.value,end=' ')
        else:
            self.printGivenLevel(node.left,level-1)
            self.printGivenLevel(node.right,level-1)
            

    def printLevelOrderBFS(self,rootNode):
        h=self.height(rootNode)
        for i in range(0,h+1):
            self.printGivenLevel(rootNode,i)


    def minValueNode(self,node):
        current=node
        while(current.left!=None):
            current=current.left
        return current
    def deleteNode(self,rootNode,value):
        if rootNode==None:return rootNode 
        elif value<rootNode.value:
            rootNode.left=self.deleteNode(rootNode.left,value)
        elif value>rootNode.value:
            rootNode.right=self.deleteNode(rootNode.right,value)
        else: 
            if rootNode.left==None:
                temp=rootNode.right
                rootNode=0 #delete rootNode
                return temp 
            elif rootNode.right==None:
                temp=rootNode.left
                rootNode=0 #delete rootNode
                return temp 
            else: 
                temp=self.minValueNode(rootNode.right)
                rootNode.value=temp.value 
                rootNode.right=self.deleteNode(rootNode.right,temp.value)
        return rootNode 


    def getBalanceFactor(self,node):
        if node==None:return -1
        else:return(self.height(node.left)-self.height(node.right))
    def rightRotate(self,yNode):
        x=yNode.left
        t2=x.right
        #perform rotation
        x.right=yNode 
        yNode.left=t2 
        return x 
    def leftRotate(self,xNode):
        y=xNode.right 
        t2=y.left
        #perform rotation 
        y.left=xNode 
        xNode.right=t2 
        return y 
    def AVLInsertionRec(self,rootNode,newNode):
        if rootNode==None:
            rootNode=newNode 
            return rootNode 
        if newNode.value<rootNode.value:
            rootNode.left=self.AVLInsertionRec(rootNode.left,newNode)
        elif newNode.value>rootNode.value:
            rootNode.right=self.AVLInsertionRec(rootNode.right,newNode)
        else: 
            print('a node with same value already exist')
            return rootNode 
        bf=self.getBalanceFactor(rootNode)
        if bf>1 and newNode.value<rootNode.left.value:
            return self.rightRotate(rootNode)
        if bf<-1 and newNode.value>rootNode.right.value:
            return self.leftRotate(rootNode)
        if bf>1 and newNode.value>rootNode.left.value:
            rootNode.left=self.leftRotate(rootNode.left)
            return self.rightRotate(rootNode)
        if bf<-1 and newNode.value<rootNode.right.value:
            rootNode.right=self.rightRotate(rootNode.right)
            return self.leftRotate(rootNode)
        return rootNode 

    def deleteNodeAVL(self,rootNode,value):
        if rootNode==None:return rootNode 
        elif value<rootNode.value:
            rootNode.left=self.deleteNode(rootNode.left,value)
        elif value>rootNode.value:
            rootNode.right=self.deleteNode(rootNode.right,value)
        else: 
            if rootNode.left==None:
                temp=rootNode.right
                rootNode=0 #delete rootNode
                return temp 
            elif rootNode.right==None:
                temp=rootNode.left
                rootNode=0 #delete rootNode
                return temp 
            else: 
                temp=self.minValueNode(rootNode.right)
                rootNode.value=temp.value 
                rootNode.right=self.deleteNode(rootNode.right,temp.value)
            
            bf=self.getBalanceFactor(rootNode)
            if bf==2 and self.getBalanceFactor(rootNode.left)>=0:
                return self.rightRotate(rootNode) 
            elif bf==2 and self.getBalanceFactor(rootNode.left)==-1:
                rootNode.left=self.leftRotate(rootNode.left)
                return self.rightRotate(rootNode)
            elif bf==-2 and self.getBalanceFactor(rootNode.right)<=0:
                return self.leftRotate(rootNode)
            elif bf==-2 and self.getBalanceFactor(rootNode.right)==1:
                rootNode.right=self.rightRotate(rootNode.left)
                return self.leftRotate(rootNode)


        return rootNode 



node1=TreeNode(20)
node12=TreeNode(10)
node13=TreeNode(30)
node14=TreeNode(8)
node15=TreeNode(12)
node16=TreeNode(40)
node17=TreeNode(28)
obj=BST()
obj.insertNode(node1)
obj.insertNode(node12)
obj.insertNode(node13)
obj.insertNode(node14)
obj.insertNode(node15)
obj.insertNode(node16)
obj.insertNode(node17)
obj.print2d(obj.root,5)
print('Pre-Order: ',end=' ')
obj.printPreOrder(obj.root)#print tree in pre-order
print()
print('In-Order: ',end=' ')
obj.printInOrder(obj.root)#print tree in in-order
print()
print('Post-Order: ',end=' ')
obj.printPostOrder(obj.root)
print()
print(obj.iterativeSearch(28))
print(obj.iterativeSearch(280))
print()
print('height of tree: ',obj.height(obj.root))
print('level-order(BFS): ',end=' ')
obj.printLevelOrderBFS(obj.root)
print()
# obj.deleteNode(obj.root,20)  #agr invalid input value doge to tree pr kuch b asr nhi hoga.
print()


nodeR=TreeNode(29)
obj.insertNodeRecursively(obj.root,nodeR)
obj.print2d(obj.root,5)
print()
print('avlinsertion')
obj2=BST()
node11=TreeNode(20)
obj2.root=obj2.AVLInsertionRec(obj2.root,node11)
node121=TreeNode(10)
node131=TreeNode(30)
node141=TreeNode(8)
node151=TreeNode(12)
node161=TreeNode(40)
node171=TreeNode(28)
obj2.AVLInsertionRec(obj2.root,node121)
obj2.AVLInsertionRec(obj2.root,node131)
obj2.AVLInsertionRec(obj2.root,node141)
obj2.AVLInsertionRec(obj2.root,node151)
obj2.AVLInsertionRec(obj2.root,node161)
obj2.AVLInsertionRec(obj2.root,node171)
obj2.print2d(obj2.root,5)
print('after deleting an item ')
obj2.deleteNodeAVL(obj2.root,20)
obj2.print2d(obj2.root,5) #will b still an AVL tree , no matter how many nodes u delete bcause of teh 
#conditions we wrote in deleteNodeAVL() f(x). 


#Heap Data Structure
from math import ceil, log2
class MinHeap:
    def __init__(self,capacity=5):
        self.harr=[None]*capacity #harr means heapArray
        self.capacity=capacity#maximum possible size of min heap
        self.heapSize=0  #current number of elements in min heap

    def linearSearch(self,val):
        for i in range(len(self.harr)):
            if self.harr[i]==val:
                print('value found: ',self.harr[i])
                return 
        print('value not found')

    def printharr(self): 
        for i in range(self.heapSize):
            print(self.harr[i],end=' ')
            
    def height(self):
        return ceil(log2(self.heapSize+1)) -1

    
    def parent(self,i):return (i-1)//2
    def left(self,i):return (2*i+1)
    def right(self,i):return (2*i+2)

    def insertKey(self,key):#insertkey means inserting a new node/value in the heap tree
        if self.heapSize==self.capacity:
            print('heap overflow')
            return 
        self.heapSize+=1
        i=self.heapSize-1
        self.harr[i]=key 
        while(i!=0 and (self.harr[self.parent(i)])>(self.harr[i])) :
            self.harr[i],self.harr[self.parent(i)]=self.harr[self.parent(i)],self.harr[i]
            i=self.parent(i)
    
    def MinHeapify(self,i):#this f(x) is to re-build/re-construct the heap tree after removing etc of an element
        l=self.left(i)
        r=self.right(i)
        smallest=i
        if l<self.heapSize and self.harr[l]<self.harr[r]:
            smallest=l
        elif r<self.heapSize and self.harr[r]<self.harr[smallest]:
            smallest=r 
        if smallest!=i:
            self.harr[i],self.harr[smallest]=self.harr[smallest],self.harr[i]
            self.MinHeapify(smallest)

    
    def extractMin(self):# remove and return the smallest value(i.e root node's value in minHeapTree)
        if self.heapSize<=0:return 'tree is empty'
        elif self.heapSize==1:
            self.heapSize-=1       #hm nei simply heapsize ko km kiya hai delete krne k liye mtlb jb koi nai value
            return self.harr[0] #aayegi to jo value extractMin ki hai uss ko override kr k heap tree mei 
        root=self.harr[0]       #add ho jaegi.
        self.harr[0]=self.harr[self.heapSize-1]
        self.heapSize-=1
        self.MinHeapify(0)
        return root 
    
    def getMin(self):return self.harr[0]

    def decreaseKey(self,index,aRandomMinNmbr):
        self.harr[index]=aRandomMinNmbr
        while(index!=0 and self.harr[self.parent(index)]>self.harr[index]):
            self.harr[index],self.harr[self.parent(index)]=self.harr[self.parent(index)],self.harr[index]
            index=self.parent(index)


    def deleteKey(self,index): #delete a particular value from the heap tree and re-build the heap tree
        self.decreaseKey(index,-1) #index means index of the key/value/item/node to be deleted from the minHeap Tree.
        self.extractMin()

    def getUnsortedArray(self):
        print('enter ',self.capacity,' values for array')
        for i in range(self.capacity):
            self.harr[i]=int(input(''))


    def heapSort(self):
        temp=[None]*self.capacity
        for j in range(self.capacity):
            temp[j]=self.extractMin()
            print(temp[j],end=' ')

obj=MinHeap()
obj.insertKey(3)
obj.insertKey(5)
obj.insertKey(8)
obj.insertKey(7)
obj.printharr()
print()
obj.linearSearch(8)
obj.extractMin()
obj.printharr()
print()
obj.deleteKey(1)
obj.printharr()

print()
objS=MinHeap()
objS.heapSize=objS.capacity
objS.getUnsortedArray()
i=objS.capacity//2-1
print('unsorted array: ')
objS.printharr()
while(i>=0):
    objS.MinHeapify(i)
    i-=1
print()
print('sorted array: ')
objS.heapSort()










#Graph
class Edge:
    def __init__(self):
        self.destinationVertexId=None 
        self.weight=None 
    
    def setEdgeValues(self,destVID,w):
        self.destinationVertexId=destVID
        self.weight=w
    def setWeight(self,w):
        self.weight=w 
    def getDestinationVertexId(self):return self.destinationVertexId
    def getWeight(self):return self.weight

class Vertex:
    def __init__(self):
        self.stateId=None 
        self.stateName=None 
        self.edgeList=[] #list of edges (edgesList)
    def getStateId(self):return self.stateId
    def getStateName(self):return self.stateName
    def setStateId(self,id):self.stateId=id
    def setStateName(self,name):self.stateName=name 
    def getEdgeList(self):
        return self.edgeList

class Graph:
    def __init__(self):
        self.allVertices=[] #dynamic array which will be storing objects of type Vertex
    
    def checkIfVertexExistById(self,vId):
        for i in range(len(self.allVertices)):
            if self.allVertices[i].getStateId()==vId:
                return True 
        return False  
    
    def addVertex(self,vertex):
        check=self.checkIfVertexExistById(vertex.getStateId())
        if check:print('a vertex with this id already exist')
        else:
            self.allVertices.append(vertex)
            print('vertex added successfully.')
    
    def printGraph(self):
        for i in range(len(self.allVertices)):
            temp=self.allVertices[i]
            print(f"{temp.getStateName()}  ({temp.getStateId()}) --> {temp.getEdgeList() }")

    def getVertexById(self,vid):
        for i in range(len(self.allVertices)):
            temp=self.allVertices[i]
            if temp.getStateId()==vid:
                return temp 
    
    def checkIfEdgeExistById(self,id1,id2):
        v=self.getVertexById(id1)
        e=v.getEdgeList()
        for it in range(len(e)):
            if e[it].getDestinationVertexId()==id2:
                return True 
        return False 
            

    def addEdgeById(self,id1,id2,w): #w=weight for e.g here it means distance from peshawar to lahor or viceversa
        check1=self.checkIfVertexExistById(id1)
        check2=self.checkIfVertexExistById(id2)

        
        if check1 and check2:
            check3=self.checkIfEdgeExistById(id1,id2)
            if check3:
                print('Edge already exist')
            else:
                for i in range(len(self.allVertices)):
                    if self.allVertices[i].getStateId()==id1:
                        self.allVertices[i].getEdgeList().append([id2,w])
                    elif self.allVertices[i].getStateId()==id2:
                        self.allVertices[i].getEdgeList().append([id1,w])
                print('Edge Added Successfully')

    

g=Graph()
v1=Vertex() 
e=Edge()
v1.setStateId(1)
v1.setStateName('Pesh')
g.addVertex(v1)

v2=Vertex() 
v2.setStateId(6)
v2.setStateName('York')
g.addVertex(v2)
g.printGraph()
g.addEdgeById(1,6,100)#100km distance from Pesh to lahore and viceversa
g.printGraph()

temp=g.getVertexById(6)
print(f"{temp.getStateName()}  ({temp.getStateId()}) --> {temp.getEdgeList() }")

print(g.checkIfVertexExistById(6))
