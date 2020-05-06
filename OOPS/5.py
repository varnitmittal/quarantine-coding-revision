#Inheritance
class A: #Super class
    def feature1(self):
        print("Feature 100")
    
    def feature2(self):
        print("Feature 200")

class B(A): #B inherits A  #single-level inheritance
    def feature3(self):
        print("Feature 300")
    def feature4(self):
        print("Feature 400")

class C(B):  #multi-level inheritance
    def feature5(self):
        print("Feature 500")

class D:
    def feature6(self):
        print("Feature 600")

class E(B, D):  #multiple-inheritance
    def feature7(self):
        print("Feature 700")


print("B class \n")
b1 = B()
b1.feature1()
b1.feature3() 

print("C class \n")
c1 = C()
c1.feature1()
c1.feature3()
c1.feature5()

print("E class \n")
e1 = E()
e1.feature1()  #from A via B
e1.feature3()  #from B
e1.feature6()  #from D
e1.feature7()
