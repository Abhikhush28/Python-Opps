"""
Now we  talk about the __str__() function.

The __str__() function controls what should be returned when the class object is represented as string.
The __str__() function is not set the string representaion of the object is returned.

"""

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def __str__(self):
        return f"{self.name}({self.age})"
    

p1 = Person("Abhishek",20)
print(p1)
