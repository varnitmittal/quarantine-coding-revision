#Constructor in Multiple Inheritance & MRO
class A: 
    def __init__(self):
        print("class A init")
    
    def feature1(self):
        print("Feature 100")
    
    def feature2(self):
        print("Feature 200")

    def same(self):
        print("the method same in class A")

class B: 
    def __init__(self):
        #super().__init__()
        print("class B init")

    def feature3(self):
        print("Feature 300")
    def feature4(self):
        print("Feature 400")

    def same(self):
        print("the method same in class B")

class C(B, A):
    def __init__(self):
        
        super().__init__()
        # displays the output
        """C class 

        class A init
        class C init"""
        # when class C(A, B) is defined
 
        #But displays the output
        """ C class 

        class B init
        class C init """
        # when class C(B, A) is defined

        # Thus, the priority of super classes 
        # folows the order of definition i.e., left to right
        # This is termed as MRO (Method Resolution Order)
        # which is applicable in cases of multiple inheritance
        # This MRO is followed by methods as well.

        super().same()
        # displays
        """ C class 

        class B init
        the method same in class B
        class C init
        the method same in class C """
        # when declared in order class C(B, A)        
 
        print("class C init")

    def feature5(self):
        print("Feature 500")

    def same(self):
        print("the method same in class C")

print("C class \n")
# Super helps us access all the elements of the super class.
c1 = C()  
""" c1.feature1()
c1.feature3() 
c1.feature5()  """

c1.same() # goes for same in C

