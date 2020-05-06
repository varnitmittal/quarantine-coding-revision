#Stack implementation thorugh array
import array as arr

class Mystack:
    def __init__(self, *args):
        self.max_size = 8
        if len(args) > self.max_size:
            print("Bounds Violation! Exiting...")
            exit(0)
        else:
            self.stack = arr.array('i', list(args))
            print(self.stack)

    def push(self, element):
        if self.isFull():
            print("Overflow!")
        else:
            self.stack.append(element)
            return self.stack

    def pop(self):
        if self.isEmpty():
            print("Underflow")
        else:
            return self.stack.pop()

    def top(self):
        if self.isEmpty():
            return "Underflow"
        else:
            return self.stack[-1]

    def isEmpty(self):
        if self.stack == []: 
            return True
        else:
            return False

    def isFull(self):
        if len(self.stack) == self.max_size:
            return True
        else:
            False

    def display(self):
        print("Final stack is " + str(self.stack))

M = Mystack(10,20,30,40,50)
print(M.isEmpty())
M.push(80)
print(M.top())
M.display()
