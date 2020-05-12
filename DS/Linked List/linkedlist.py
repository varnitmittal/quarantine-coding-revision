# My own implementation of Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def append(self, data):  # adds node to the end of the list
        if self.isEmpty():
            self.head = Node(data)
            return
        curr = self.head
        while(curr.next):
            curr = curr.next
        curr.next = Node(data)

    def prepend(self, data):  # adds node to the beginning of the list
        if self.isEmpty():
            self.head = Node(data)
            return
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def addAtIndex(self, index, data):  #adds node somewhere in between the list
        if self.isEmpty():
            self.head = Node(data)
            return
        curr = self.head
        for x in range(index-1):  # indexing is same as that of arrays
            curr = curr.next
        temp = Node(data)
        temp.next = curr.next
        curr.next = temp

    def deleteFirst(self):
        if self.isEmpty():
            print("\tUnderflow! List is already empty.")
            return
        print("\tThe node deleted is ", self.head.data, " from index 0.")
        self.head = self.head.next

    def deleteAtIndex(self, index):
        if self.isEmpty():
            print("\tUnderflow! List is already empty.")
            return 
        elif index >= self.length():
            print("the element doesn't exist")
            return
        else:
            curr = self.head
            for x in range(index-1):  # indexing is same as that of arrays
                curr = curr.next
            print("\tThe node deleted is ", curr.next.data, " from index ", index)
            curr.next = curr.next.next

    def length(self):
        if self.isEmpty():
            print("The list is empty.")
            return
        curr = self.head
        count = 1
        while(curr.next):
            curr = curr.next
            count += 1
        return count
    
    def findKey(self, key):
        if self.isEmpty():
            print("The list is empty. No key found.")
            return
        count = 0
        curr = self.head
        while(curr.next):
            if curr.data == key:
                print("\t", key, " found at index", count)              
                return
            curr = curr.next
            count += 1

    def reverse(self):
        if self.isEmpty():
            print("List is empty, nothing to reverse")
            return
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next      #linking to next node & shifting next node by one place
            curr.next = prev_node      #reversing the previous link
            prev_node = curr           #shifting previous node by one place
            curr = next_node           #shifting current node by one place
        self.head = prev_node          #finally making the last node the head

    def display(self):
        temp = self.head
        while(temp):
            print(temp.data, end="  ")
            temp = temp.next
        print("\n")

M = MyLinkedList()
M.head = Node(10)
second = Node(20)
third = Node(30)

M.head.next = second
second.next = third

M.display()

M.append(40)
M.append(50)
M.display()

M.prepend(8)
M.prepend(4)
M.display()

M.addAtIndex(2, 100)
M.display()

M.deleteFirst()
M.display()
M.deleteAtIndex(3)
M.display()

print("Length of list is: ", M.length())
for key in [40, 8]:
    M.findKey(key)

print("The original list: ")
M.display()
M.reverse()
print("The reversed list: ")
M.display()





"""OUTPUT
10  20  30  

10  20  30  40  50  

4  8  10  20  30  40  50  

4  8  100  10  20  30  40  50  

	The node deleted is  4  from index 0.
8  100  10  20  30  40  50  

	The node deleted is  20  from index  3
8  100  10  30  40  50  

Length of list is:  6
	 40  found at index 4
	 8  found at index 0
The original list: 
8  100  10  30  40  50  

The reversed list: 
50  40  30  10  100  8  
"""