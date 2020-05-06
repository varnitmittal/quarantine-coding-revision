#Operator Overloading

#Examples that usually exist
""" 
2+3 = 5 
2+3.6 = 5.6
hello+world = helloworld
"""

#this is where we need operator overloading 
# to explicitly specify its behavior in 
# such unconventional cases
"""
2+"world" = !ERROR 
"""

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def get_marks(self):
        print("marks are " + str(self.m1) + " and" + str(self.m2))

    def __add__(self, other):  
        # First oprand goes into self 
        # and Second operand goes into other

        new_m1 = (self.m1 + other.m1)/2
        new_m2 = (self.m2 + other.m2)/2
        s_new = Student(new_m1, new_m2)
        return s_new

    def __gt__(self, other):
        # First oprand goes into self 
        # and Second operand goes into other

        # Let's say we decide to compare total marks of 2 students
        s1_total = self.m1 + self.m2
        s2_total = other.m1 + other.m2
        if s1_total > s2_total:
            return True
        else:
            return False

s1 = Student(58,69)
s2 = Student(60,65)

s3 = s1+s2  # Overloaded operator +

s3.get_marks()

if s1 > s2:  # Overloaded operator >
    print("Student 1 tops")
elif s2 > s1:
    print("Student 2 tops")
else:
    print("Tie")