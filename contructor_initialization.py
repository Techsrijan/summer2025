class Dog:
    def __init__(self, name, breed): # parametrize constuctor
        self.name = name  # Initialize the 'name' attribute
        self.breed = breed  # Initialize the 'breed' attribute
        print(f"{self.name} the {self.breed} has been created!")
        print(self.name,"the ",self.breed," has been created!")

# Creating an instance of the Dog class, which calls the __init__ method
my_dog = Dog("Buddy", "Golden Retriever")

# Accessing attributes initialized by the constructor
print(f"My dog's name is {my_dog.name} and its breed is {my_dog.breed}.")