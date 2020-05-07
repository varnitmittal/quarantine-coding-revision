#Deque implementation

class Deque:
    def __init__(self, *args):
        self.max = 5
        self.deque = []
        self.front = -1
        self. rear = -1
        self.display()

    def isFull(self):
        return False
    
    def insertFront(self, x):
        if self.isFull():
            print("Can't insert, deque is already full.")
        elif len(self.deque) == 0:
            self.deque.insert(0, x)
            self.rear = 0
            self.front = 0            
        else:
            self.deque.insert(0, x)
            self.front 

    def deleteFront(self):
        if self.isEmpty():
            print("Deque is already empty")
        else:
            self.deque.pop(0)

    def isEmpty(self):
        return False

    def insertRear(self, x):
        if self.isFull():
            print("Can't insert, deque is already full.")
        else:
            self.deque.append(x)

    def deleteRear(self):
        if self.isEmpty():
            print("Deque is already empty")
        else:
            self.deque.pop()

    def peekFront(self):
        pass

    def peekRear(self):
        pass

    def display(self):
        print(self.deque)

D = Deque()
D.insertFront(10)
D.insertRear(20)
D.insertRear(30)
D.insertRear(40)
D.insertRear(50)
D.insertRear(60)
D.insertRear(70)
D.display()
D.deleteRear()
D.deleteFront()
D.display()