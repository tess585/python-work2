# Create a calculator code in which i input the first number the second number and the operator and it gives me the result
x = float(input("entter first number:"))
y = float(input("enter second number:"))
operator = input("enter operator:")
if operator == "+":
    print("result is:", x+y)
if operator == "-":
    print("result is:", x-y)
if operator == "*":
    print("result is:", x*y)
if operator == "/":
    print("result is:", x/y)
if operator == "%":
    print("result is:", x%y)
else:
    print("invalid operator")
