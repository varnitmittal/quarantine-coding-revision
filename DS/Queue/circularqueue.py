#My own implementation of circular queue using python list/array

class MyCircularQueue:
    def __init__(self, *args):
        self.max = 5
        self.circular = list(range(self.max))

        if len(args) > self.max:
            print("Bounds Violated. Exiting...")
            exit(0)
        else:
            for i in range(len(args)):
                self.circular[i] = list(args)[i]
            # we put both front and rear as -1 for empty queue
            # but here the queue is initialized differently
            self.front = 0
            self. rear = len(args) - 1  
            print("Circular Queue of max length {} is ready. \n".format(self.max))
            self.display()
    
    def isFull(self):
        if (self.rear + 1) % self.max == self.front:
            print("\tOverflow!")
            return True        
        else:
            return False

    def enqueue(self, x):
        if self.isFull():
            print("\tCan't add element {} as the circular queue is full.\n".format(x))        
        
        elif self.rear == -1 & self.front ==-1:    #no element in queue
            self.front = self.rear = 0
            self.circular[self.rear] = x
            print("\n\tAdded element", x, " at index ", self.rear)

        else:
            self.rear = (self.rear + 1) % self.max  #this is what makes it circular
            self.circular[self.rear] = x
            print("\n\tAdded element", x, " at index ", self.rear)
        
    def isEmpty(self):
        if (self.front == -1 & self.rear == -1):
            print("\tUnderflow")
            return True       
        else:
            return False
    
    def dequeue(self):
        if self.isEmpty():   #no element in queue
            print("\tCan't delete element as the circular queue is empty.")
        
        elif self.front == self.rear:   #single element in queue
            print("\t", self.circular[self.front], "is deleted from index ", self.front," The queue is empty now")
            self.front = self.rear = -1 #no element is left now

        else:
            print("\t", self.circular[self.front], "is deleted from index ", self.front)
            self.front = (self.front + 1) % self.max  #this is what makes it circular


    def display(self):
        print("\nDISPLAY:")     
        if self.isEmpty():
            print("The queue is empty, nothing to display.")
            print("front is at index ", self.front)
            print("rear is at index ", self.rear)
        
        elif self.rear >= self.front:
            print("The circular queue is ") 
            for i in range(self.front, self.rear + 1): 
                print(self.circular[i], end = "  ")
            print("\nfront is at index ", self.front)
            print("rear is at index ", self.rear) 
        
        else:    
            print("The circular queue is ")
            for i in range(0, self.rear + 1): 
                print(self.circular[i], end = " ")
            for i in range(self.front, self.max): 
                print(self.circular[i], end = " ") 
            print("\nfront is at index ", self.front)
            print("rear is at index ", self.rear)

C = MyCircularQueue(10, 20, 30)

C.enqueue(60)
C.enqueue(70)
C.enqueue(80)
C.display()

C.dequeue()
C.dequeue()
C.dequeue()
C.display()

C.enqueue(90)
C.enqueue(100)
C.display()

C.dequeue()
C.dequeue()
C.dequeue()
C.display()




"""OUTPUT
Circular Queue of max length 5 is ready. 


DISPLAY: [10, 20, 30, 3, 4]
A
The circular queue is 
10  20  30  
front is at index  0
rear is at index  2

	Added element 60  at index  3

	Added element 70  at index  4
	Overflow!
	Can't add element 80 as the circular queue is full.


DISPLAY: [10, 20, 30, 60, 70]
A
The circular queue is 
10  20  30  60  70  
front is at index  0
rear is at index  4
	 10 is deleted from index  0
	 20 is deleted from index  1
	 30 is deleted from index  2

DISPLAY: [10, 20, 30, 60, 70]
A
The circular queue is 
60  70  
front is at index  3
rear is at index  4

	Added element 90  at index  0

	Added element 100  at index  1

DISPLAY: [90, 100, 30, 60, 70]
B
The circular queue is 
90 100 60 70 
front is at index  3
rear is at index  1
	 60 is deleted from index  3
	 70 is deleted from index  4
	 90 is deleted from index  0

DISPLAY: [90, 100, 30, 60, 70]
A
The circular queue is 
100  
front is at index  1
rear is at index  1

"""