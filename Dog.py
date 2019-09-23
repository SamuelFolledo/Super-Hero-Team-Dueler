#Dog.py
class Dog:
    def __init__(self, name, breed): #__init__ is a constructor, which is a method that runs whenever a new instance of your class is created
        self.name = name
        self.breed = breed
    
    def bark(self):
        print("Woof!")

    def roll(self):
        print("rolls over")

    def sit(self):
        print("sits")
