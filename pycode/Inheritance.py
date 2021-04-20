class phone:
    def call(self):
        print("you can't call")

    def Message(self):
        print("Pls text me")


class Aphone(phone):  # inherit phone class
    # message,call

    def call(self):
        super().call()
        print("you can now call")

    def video_call(self):
        print("pls on your camera")


p = phone()
#p.call()
#p.Message()

#print(" ")
A = Aphone()
for mobile in (p,A):
    mobile.call()
    mobile.Message()
    #mobile.video_call()
#A.Message()
#A.call()
#A.video_call()

print(issubclass(Aphone,phone))
print("''''''''''''''''''''''''''''''''''''''''''''''")
# calculate area of triangle and ractangle
from abc import ABC,abstractmethod
class shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    @abstractmethod
    def area(self):
        pass


class Triangle(shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of triangle : ",area)

class Ractangle(shape):
    def area(self):
        area =  self.dim1 * self.dim2
        print("Area of Ractangle : ",area)

t = Triangle(20,30)
#t.area()

r = Ractangle(20,30)
#r.area()
for calculate in (t,r):
    #print(" ")
    calculate.area()

