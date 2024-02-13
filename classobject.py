#A class is a blueprint of an object
#An object is an instance of a class

class person:
# properties/Atributes/Variables/Characteristics
    name = "joe"
    age = 24

# Method/Function/Behaviour
    def talk(self):
     print("Person is talking")

teacher = person()
print(teacher.name)
print(teacher.age)

teacher.talk()