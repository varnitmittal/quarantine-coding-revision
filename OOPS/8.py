#Polymorphism =>
"""
Duck Typing
Operator Overloading
Method Overloading
Method Overriding
"""

#Duck Typing
class Atom:
    def execute(self):
        print("compiling")
        print("running")

class Sublime:
    def execute(self):
        print("File check")
        print("compiling")
        print("running")

class Laptop:
    def code(self, ide):
        ide.execute()

ide = Sublime()

lap1 = Laptop()
#lap1.code(ide)  in this, we have to pass ide which 
# is an object of class Sublime which is fixed, but 
# in case we need to dynamically change the ide in 
# future; we need to have some object that has execute.
# According to duck typing, as long as an execute method 
# exists in a class, its object will work for the class Laptop 
lap1.code(ide)

