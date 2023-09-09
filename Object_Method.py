"""
Object Method:

object Methods can also contains method in objects are function that belong to the objects

Insert function that print a greeting and executing it on the p1 object

"""

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def myfunc(self):
        print("Hello my name is "+self.name)
    

p1 = Person("Abhishek",20)
p1.myfunc()
