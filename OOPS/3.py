#Static Method
class Student:

    school = "MySchool"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    @staticmethod
    def info():
        print("This is Student class in abc module")

    @classmethod
    def get_school_name(cls):
        return cls.school

    @classmethod
    def set_school_name(cls):
        cls.school = "New School"


s1 = Student(34,67,32)
s2 = Student(99,32,12)

print(Student.get_school_name())
Student.set_school_name()
print(Student.get_school_name())

Student.info()