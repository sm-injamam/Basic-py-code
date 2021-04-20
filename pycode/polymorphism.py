"""
Below code shows how python can use two different class types, in the same way.
We create a for loop that iterates through a tuple of objects.
Then call the methods without being concerned about which class type each object is.
 We assume that these methods actually exist in each class.
"""


class India():
    def capital(self):
        print("Dhaka is the capital of Bangladesh.")

    def language(self):
        print("Bangla is the mother tongue of Bangladesh.")

    def type(self):
        print("Bangladesh is a developing country.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):  # using for loop
    country.capital()
    country.language()
    country.type()
