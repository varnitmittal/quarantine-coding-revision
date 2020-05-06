#Instance & Class Variables
class Cars:
    wheels = 4

    def __init__(self, mil,model):
        self.mil = mil
        self.model = model

c1 = Cars(11, "asdf")
c2 = Cars(16, "zxcv")

print(c1.mil, c1.model, c1.wheels)
print(c2.mil, c2.model, c2.wheels)

c1.mil = 9
#c1.wheels = 13
print(c1.mil, c1.model, c1.wheels)
print(c2.mil, c2.model, c2.wheels)

Cars.wheels = 3
print(c1.mil, c1.model, c1.wheels)
print(c2.mil, c2.model, c2.wheels)

c1.wheels = 13
print(c1.mil, c1.model, c1.wheels)
print(c2.mil, c2.model, c2.wheels)


print(c1.wheels)
print(c2.wheels)
print(Cars.wheels)

Cars.wheels = 3
print(c1.mil, c1.model, c1.wheels)
print(c2.mil, c2.model, c2.wheels)