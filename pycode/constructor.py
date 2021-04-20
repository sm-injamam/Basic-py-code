
class Triangle:

   def __init__(self,base,height):
        self.base = base
        self.height = height

   def calculate_area(self):
        area = 0.5 * self.base * self.height

        print("Area = ",area)
        return(f"The Base is {self.base} and The Hieght is {self.height} ")


t1 = Triangle(10,20)
print(t1.calculate_area())

print(" ")

t2=Triangle(30,40)
t2.calculate_area()


