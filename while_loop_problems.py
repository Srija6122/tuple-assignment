import random

# 1. Print numbers from 1 to n using while loop

def print_numbers(n):
    count = 1
    while count <= n:
        print(count)
        count += 1

num = int(input("Enter a positive integer: "))
if num > 0:
    print("\nNumbers from 1 to", num)
    print_numbers(num)
else:
    print("Please enter a positive integer.")


# 2. Simple Bank Account System

balance = 1000

while True:
    print("\nBank Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Deposit Successful.")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful.")
        else:
            print("Insufficient Balance.")

    elif choice == "3":
        print("Current Balance: $", balance)

    elif choice == "4":
        print("Thank you for using the bank system.")
        break

    else:
        print("Invalid Choice.")


# 3. Factorial using while loop

def find_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    return fact

number = int(input("\nEnter a number to find factorial: "))
try:
    print("Factorial:", find_factorial(number))
except ValueError as e:
    print(e)


# 4. Number Guessing Game

secret = random.randint(1, 100)

print("\nGuess the number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret:
        print("Higher")
    elif guess > secret:
        print("Lower")
    else:
        print("Correct! You guessed the number.")
        break