"""
        OOPS in Python
To understand the meaning of classes we have to understand the built-in __init__() function.

All class have a function called __init__(), which is always executed when the class is being initiated.

use the __init__() function to assign values to object properties or other operators that are necessary to 
do when the object is begin created.




"""

class Person:
    #look like a constructor in other language
    def __init__(self, name, age):
        self.name=name
        self.age=age

p1 = Person("Abhishek", 20)
print(p1.name)
print(p1.age)
