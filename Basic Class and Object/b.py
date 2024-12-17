# Define a class
class Dog:
    # init method
    def __init__(self, name):
        self.name = name
    

    def bark(self):
        print(f"{self.name} says Woof!")

# Create an object of the class
# my dog
my_dog = Dog("Buddy")
# bark
my_dog.bark()