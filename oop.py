class person:
    def __init__(self, firstname, age, gender):
        self.firstname = firstname
        self.age = age
        self.gender = gender
    def details(self):
        print(self.firstname,"is studying")
teacher = person("John",25,"male")
accountant = person("Mary",26,"Female")
Doctor = person("Joe",62,"male")

print(teacher.firstname,teacher.age,teacher.gender)
print(accountant.firstname,accountant.age,accountant.gender)
print(Doctor.firstname,Doctor.age,Doctor.gender)

teacher.details()