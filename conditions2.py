# 1. Compare Two Numbers

def compare_numbers(a, b):
    if a > b:
        print(a, "is larger")
    elif b > a:
        print(b, "is larger")
    else:
        print("Both numbers are equal")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
compare_numbers(num1, num2)


# 2. Logical Operators

number = int(input("Enter a number: "))
if 10 <= number <= 20:
    print("Number is between 10 and 20")
else:
    print("Number is outside the range")

text = input("Enter a string: ")
if text and len(text) > 5:
    print("String is valid")
else:
    print("String is not valid")


# 3. Simple Calculator

operation = input("Enter operation (+, -, *, /): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if operation == "+":
    print("Result:", a + b)
elif operation == "-":
    print("Result:", a - b)
elif operation == "*":
    print("Result:", a * b)
elif operation == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")


# 4. Age Classification

age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")


# 5. Simple Login System

username = input("Enter username: ")
password = input("Enter password: ")

correct_username = "admin"
correct_password = "1234"

if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")