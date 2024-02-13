# Data type
number = 67 # int
num = 78.98 # float
greeting = "Hello there" #str
isPythonInteresting = True #bool

# A variable storing multiple values
languages = ["Python", "PHP", "Java"] #list
fruits = ["banana","apple","pineapple"] #tuple
countries = {"Kenya", "China", "North America"} #sets

# Dictionary
details = {
    "firstname": "Brian",
    "age": 17,
    "course": "MIT",
    "Nationality": "Kenyan"
}

print(number)
print(isPythonInteresting)
print(countries)
print(details)
print(details["course"])
print(details["Nationality"])

# Determining the data type
print(type(details))
print(type(countries))
print(type(languages))

# Typecasting - Converting one data type to another
print(float(number))
print(int(num))

