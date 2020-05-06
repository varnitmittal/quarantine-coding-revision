#Method Overloading & Method Overriding

# Python DOES NOT support method overloading
# We can overload a method of course, but
# Python only considers the lastest defined 
# method only, regardless of the number of
# paramters involved.
# However, it does support method overriding


#Method Overloading
def product(a, b): 
    p = a * b 
    print(p) 

def product(a, b, c): 
    p = a * b*c 
    print(p) 
  
# product(4, 5)  #!ERROR  
product(4, 5, 5) # Works fine



#Method Overriding
class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):  #overriden
        super().show()  # calling parent class method 
        print("in B show")

b1 = B()
b1.show()