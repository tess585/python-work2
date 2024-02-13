# Inbuilt functions
number = max(34, 78,90,123,45)
print(number)

y = min(45, 78, 34, 23)
print(y)

z = pow(2, 3)
print(z)

# User-defined function
def name():
    print("Stacy")
name() # Calling a function

def details():
    name = "Tess"
    age = 20
    course = "MIT"
    print(name, age, course)
details() # calling a function

# Parameters/variables and argument/variables
def patient(name, age, gender,marriage_status):
    print(name, age, gender,marriage_status)
patient("tess","38","female","sinle")
patient("job","48","male","married")

def multiply(x,y):
    print(x*y)

multiply(2,6)
multiply(12,6)
multiply(21,60)
multiply(15,3)

# Create a user-defined function. Called employees
def employees(fullname,salary, age, position, gender):
    print(fullname,salary, age, position, gender)
employees("Carol","20000",29,"Manager","Female")
employees("Tess","30000",39,"CEO","Female")
employees("John","40000",35,"Security","Male")
employees("Jane","100000",24,"Instructor","Female")
employees("Peterson","60000",39,"Manager","male")