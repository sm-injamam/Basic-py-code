class phone:
    def __init__(self):
        print("I am phone class")

class iphone(phone):

    def __init__(self):
        super().__init__()

        print("overriding here")


    def costly(self):
        print("I am Iphone class")

p = phone()
print("from here starting Iphone class ")
i = iphone()
i.costly()
