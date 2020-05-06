#Constructor in Single-Level Inheritance
class A: #Super class
    def __init__(self):
        print("class A init")
    
    def feature1(self):
        print("Feature 100")
    
    def feature2(self):
        print("Feature 200")

class B(A): #B inherits A  #single-level inheritance
    def __init__(self):
        super().__init__()
        print("class B init")

    def feature3(self):
        print("Feature 300")
    def feature4(self):
        print("Feature 400")

print("B class \n")
# If we instantiate B without specifying any contructor in B, 
# it automatically calls the super class contructor
# If init of B exists, it won't go for super class init
# In order to explicitly call the super class contructor, we use 
# super().__init__
# Super helps us access all the elements of the super class.
b1 = B()  
#b1.feature1()
#b1.feature3() 
