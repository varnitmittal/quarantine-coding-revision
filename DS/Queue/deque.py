#My own implementation of double-ended circular queue using python list/array

class MyDeque:
    def __init__(self, *args):
        self.max = 5
        self.deque = list(range(self.max))

        if len(args) > self.max:
            print("Bounds Violated. Exiting...")
            exit(0)
        elif len(args) == 0:
            self.front = self. rear = - 1  
            print("Deque of max length {} is ready. \n".format(self.max))
            self.display()
        else:
            for i in range(len(args)):
                self.deque[i] = list(args)[i]
            # we put both front and rear as -1 for empty queue
            # but here the queue is initialized differently
            self.front = 0
            self. rear = len(args) - 1  
            print("DeQue of max length {} is ready. \n".format(self.max))
            self.display()
    
    def isFull(self):
        if (self.rear + 1) % self.max == self.front:
            print("\tOverflow!")
            return True        
        else:
            return False

    def enqueueFront(self, x):
        if self.isFull():
            print("\tCan't add element {} as the deque is full.\n".format(x))        
        
        elif self.rear == -1 & self.front == -1:    #no element in queue
            self.front = self.rear = 0
            self.deque[self.front] = x
            print("\n\tAdded element", x, " at index ", self.front)

        else:
            if self.front == 0:
                self.front = self.max - 1    #this is what makes it deque
                #self.rear = (self.rear + 1) % self.max  
                self.deque[self.front] = x
                print("\n\tAdded element", x, " at index ", self.front)
            else:
                self.front -= 1
                self.deque[self.front] = x
                print("\n\tAdded element", x, " at index ", self.front)

    def enqueueRear(self, x):
        if self.isFull():
            print("\tCan't add element {} as the deque is full.\n".format(x))        
        
        elif self.rear == -1 & self.front ==-1:    #no element in queue
            self.front = self.rear = 0
            self.deque[self.rear] = x
            print("\n\tAdded element", x, " at index ", self.rear)

        else:
            if self.rear == self.max - 1:
                self.rear = 0    #this is what makes it deque
                #self.rear = (self.rear + 1) % self.max  
                self.deque[self.rear] = x
                print("\n\tAdded element", x, " at index ", self.rear)
            else:
                self.rear += 1
                self.deque[self.rear] = x
                print("\n\tAdded element", x, " at index ", self.rear)
    
    def isEmpty(self):
        if (self.front == -1 & self.rear == -1):
            print("\tUnderflow")
            return True       
        else:
            return False
    
    def dequeueFront(self):
        if self.isEmpty():
            print("\tCan't delete element as the deque is empty.")
        
        elif self.rear == self.front:    #one element in queue
            print("\t", self.deque[self.front], "is deleted from index ", self.front," The queue is empty now")
            self.front = self.rear = -1 #no element is left now

        else:
            if self.front == self.max - 1:
                print("\t", self.deque[self.front], "is deleted from index ", self.front)
                self.front = 0  #this is what makes it circular
            else:
                print("\t", self.deque[self.front], "is deleted from index ", self.front)
                self.front += 1

    def dequeueRear(self):
        if self.isEmpty():
            print("\tCan't delete element as the deque is empty.")
        
        elif self.rear == self.front:    #one element in queue
            print("\t", self.deque[self.rear], "is deleted from index ", self.rear," The queue is empty now")
            self.front = self.rear = -1 #no element is left now

        else:
            if self.rear == 0:
                print("\t", self.deque[self.rear], "is deleted from index ", self.rear)
                self.rear = self.max - 1  #this is what makes it circular
            else:
                print("\t", self.deque[self.rear], "is deleted from index ", self.rear)
                self.rear -= 1

    def display(self):
        print("\nDISPLAY:")     
        if self.isEmpty():
            print("The queue is empty, nothing to display.")
            print("front is at index ", self.front)
            print("rear is at index ", self.rear)
        
        elif self.rear >= self.front:
            print("The deque is ") 
            for i in range(self.front, self.rear + 1): 
                print(self.deque[i], end = "  ")
            print("\nfront is at index ", self.front)
            print("rear is at index ", self.rear) 
        
        else:    
            print("The deque is ")
            for i in range(0, self.rear + 1): 
                print(self.deque[i], end = " ")
            for i in range(self.front, self.max): 
                print(self.deque[i], end = " ") 
            print("\nfront is at index ", self.front)
            print("rear is at index ", self.rear)

C = MyDeque()

C.enqueueFront(10)
C.enqueueRear(100)
C.enqueueFront(20)
C.enqueueRear(90)
C.enqueueRear(80)
C.enqueueFront(30)
C.display()

C.dequeueRear()
C.dequeueFront()
C.dequeueRear()
C.display()

C.dequeueRear()
C.dequeueFront()
C.dequeueRear()
C.display()





"""OUTPUT
Deque of max length 5 is ready. 


DISPLAY:
	Underflow
The queue is empty, nothing to display.
front is at index  -1
rear is at index  -1

	Added element 10  at index  0

	Added element 100  at index  1

	Added element 20  at index  4

	Added element 90  at index  2

	Added element 80  at index  3
	Overflow!
	Can't add element 30 as the deque is full.


DISPLAY:
The deque is 
10 100 90 80 20 
front is at index  4
rear is at index  3
	 80 is deleted from index  3
	 20 is deleted from index  4
	 90 is deleted from index  2

DISPLAY:
The deque is 
10  100  
front is at index  0
rear is at index  1
	 100 is deleted from index  1
	 10 is deleted from index  0  The queue is empty now
	Underflow
	Can't delete element as the deque is empty.

DISPLAY:
	Underflow
The queue is empty, nothing to display.
front is at index  -1
rear is at index  -1

"""