#Inner Classes
class Student: #outer class    
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop(brand="DELL")  #Instantiation within the Outer Class

    def show1(self):
        print(self.name, self.rollno, self.lap.cpu)
        self.lap.show_laptop()

    #def show2(self, lapobj):
        #print(self.name, self.rollno, lapobj.cpu)

    class Laptop: #inner class
        def __init__(self, brand = 'HP', cpu='i5', ram='8gb'):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
        
        def show_laptop(self):
            print(self.brand, self.cpu, self.ram) 


s1 = Student("Navin", 2)
s2 = Student("Jenny", 3)

print(s1.lap.ram)

s1.show1()
s2.show1()

lap2 = Student.Laptop(cpu='i9') #Instantiation outside the Outer Class
lap3 = Student.Laptop(cpu='pentium') #Instantiation outside the Outer Class
#s1.show2(lap2)
#s2.show2(lap3)

lap2.show_laptop()
lap3.show_laptop()