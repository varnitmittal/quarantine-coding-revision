#stack with LIFO queue

import queue  #inbuilt library

a = queue.LifoQueue(maxsize=7)  #initialization of stack

a.put(10)  #enqueue
a.put(8)
a.put(17)
a.put(22)
a.put(3)

print(a.queue)
print("Size is ", a.qsize())
print("Full?", a.full())

a.put(13)
a.put(31)

print(a.queue)
print("Size is ", a.qsize())
print("Full?", a.full())


print(a.get())  #dequeue
print(a.get())
print(a.get())
print(a.get())
print(a.get())
print(a.get())
print(a.get())

print(a.queue)
print("Size is ", a.qsize())

if a.queue:
    print(a.get()) 
else:
    print("Underflow")

if a.empty:
    print("Underflow")
else:
    print(a.get()) 



"""OUTPUT
[10, 8, 17, 22, 3]
Size is  5
Full? False
[10, 8, 17, 22, 3, 13, 31]
Size is  7
Full? True
31
13
3
22
17
8
10
[]
Size is  0
Underflow
Underflow
"""