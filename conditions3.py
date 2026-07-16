import random

# 1. Voting Eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# 2. Letter Grade Function

def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

marks = float(input("\nEnter your percentage: "))
print("Your Grade:", get_grade(marks))


# 3. Simple Calculator

print("\nCalculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print("Result:", num1 + num2)
elif choice == "2":
    print("Result:", num1 - num2)
elif choice == "3":
    print("Result:", num1 * num2)
elif choice == "4":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid choice.")


# 4. Random Number Odd or Even

random_number = random.randint(1, 100)

print("\nGenerated Number:", random_number)

if random_number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")