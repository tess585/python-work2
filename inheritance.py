#Parent class/Super class/Base class
class Animal:
    def sound(self):
       print("Animal is speaking")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")
#Child class/Sub class/ Derived class
class cat(Animal):
    def meow(self):
        print("A cat is meowing")

a = Animal()
d = Dog()
d.sound()
c = cat()
c.sound()