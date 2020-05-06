#Instance & Class Methods
class Student:

    school = "MySchool"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    def get_marks(self):
        print(self.m1, self.m2, self.m3)
    
    def get_m3(self):  #accessor methods
        print(self.m3)
    
    def get_m2(self):  #accessor methods
        print(self.m2)

    def set_m3(self):  #mutator methods
        self.m3 += 10
        self.get_m3()

    def set_m2(self, value):
        self.m2 = value

    @classmethod
    def get_info(cls):
        return cls.school

    @classmethod
    def set_info(cls):
        cls.school = "New School"


s1 = Student(34,67,32)
s2 = Student(99,32,12)
""" 
print(s1.avg())
print(s2.avg())

s1.get_m3()
s2.get_m3()

s1.set_m3()
s2.set_m3()

s1.set_m2(69)
s2.set_m2(34)

s1.get_m2()
s2.get_m2()

s1.get_marks()
s2.get_marks()
 """
print(Student.get_info())
Student.set_info()
print(Student.get_info())