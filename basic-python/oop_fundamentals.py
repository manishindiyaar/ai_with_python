# Object-Oriented Programming (OOP) Fundamentals

# Classes
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


 
# Inheritance
class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Encapsulation
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # The underscore prefix is a convention to indicate a protected member

    def display_info(self):
        return f"Name: {self.name}, Age: {self._age}"



# Polymorphism
def animal_sound(animal):
    print(animal.speak())

# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
person = Person("John", 30)

print(dog.speak())
print(cat.speak())
print(person.display_info())
animal_sound(dog)
animal_sound(cat)
