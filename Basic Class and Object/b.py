# Define a class
class Dog:
    def __init__(self, name):
        self.name = name
    

    def bark(self):
        print(f"{self.name} says Woof!")

# Create an object of the class

my_dog = Dog("Buddy")

my_dog.bark()