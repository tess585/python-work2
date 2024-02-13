temperature = 34

if temperature > 25 :
    print("it is hot")
else :
    print("it is cold")

# A program that determines the largest number
num1 = 78
num2 = 90
num3 = 23
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3,"is the largest number")

# A Program that checks whether a number is odd or even
number = 20

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# A program that checks whether a number is a prime number or not
num =13
if num > 1:
    for x in range (2, num):
        if num % x == 0:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
    break
else:
print("the number is not a prime number")
