# 1. Positive, Negative or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 2. Even or Odd
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

# 3. Voting Eligibility
age = int(input("Enter age: "))
print("Eligible to Vote" if age >= 18 else "Not Eligible")

# 4. Greater of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Greater:", a if a > b else b)

# 5. Divisible by 5
num = int(input("Enter number: "))
print("Divisible by 5" if num % 5 == 0 else "Not Divisible by 5")

# 6. Multiple of 3
num = int(input("Enter number: "))
print("Multiple of 3" if num % 3 == 0 else "Not multiple of 3")

# 7. Vowel or Consonant
ch = input("Enter character: ").lower()
if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# 8. Greater than 100
num = int(input("Enter number: "))
print("Greater than 100" if num > 100 else "Not Greater than 100")

# 9. Leap Year
year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# 10. Temperature
temp = int(input("Enter temperature: "))
print("Hot" if temp > 30 else "Cold")

# 11. Grade
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# 12. Calculator
a = float(input("First number: "))
op = input("Operator (+,-,*,/): ")
b = float(input("Second number: "))
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid Operator")

# 13. FizzBuzz
num = int(input("Enter number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

# 14. Character Type
ch = input("Enter character: ")
if 'A' <= ch <= 'Z':
    print("Uppercase")
elif 'a' <= ch <= 'z':
    print("Lowercase")
elif '0' <= ch <= '9':
    print("Digit")
else:
    print("Special Character")

# 15. Tax Percentage
salary = float(input("Enter salary: "))
if salary < 250000:
    print("No Tax")
elif salary <= 500000:
    print("5% Tax")
elif salary <= 1000000:
    print("20% Tax")
else:
    print("30% Tax")

# 16. Largest of Three
a = int(input())
b = int(input())
c = int(input())
if a > b:
    if a > c:
        print("Largest:", a)
    else:
        print("Largest:", c)
else:
    if b > c:
        print("Largest:", b)
    else:
        print("Largest:", c)

# 17. Login
user = input("Username: ")
pwd = input("Password: ")
if user == "admin" and pwd == "1234":
    print("Login Success")
else:
    print("Login Failed")

# 18. Positive then Even/Odd
num = int(input("Enter number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Not Positive")

# 19. ATM
balance = 10000
amount = float(input("Withdraw amount: "))
if amount <= balance:
    if amount <= 5000:
        print("Transaction Successful")
    else:
        print("Withdrawal limit exceeded")
else:
    print("Insufficient Balance")

# 20. Student Result
marks = int(input("Enter marks: "))
if marks >= 35:
    print("Pass")
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
else:
    print("Fail")

# 21. 3-digit Number
num = int(input("Enter number: "))
print("3-digit" if 100 <= abs(num) <= 999 else "Not 3-digit")

# 22. Valid Triangle
a = int(input())
b = int(input())
c = int(input())
if a + b + c == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

# 23. Second Largest
nums = [int(input()), int(input()), int(input())]
nums.sort()
print("Second Largest:", nums[1])

# 24. Alphabet Check
ch = input("Enter character: ")
if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
    print("Alphabet")
else:
    print("Not Alphabet")

# 25. Electricity Bill
units = int(input("Enter units: "))
if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 5
else:
    bill = 100 * 5 + (units - 200) * 10
print("Bill =", bill)

# 26. Movie Ticket
age = int(input("Enter age: "))
if age < 12:
    print("Child Ticket")
elif age > 60:
    print("Senior Ticket")
else:
    print("Adult Ticket")

# 27. Login with 3 Attempts
username = "admin"
password = "1234"
for i in range(3):
    u = input("Username: ")
    p = input("Password: ")
    if u == username and p == password:
        print("Login Successful")
        break
else:
    print("Account Locked")

# 28. Palindrome
num = input("Enter number: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 29. Shopping Discount
amount = float(input("Shopping amount: "))
if amount >= 5000:
    discount = amount * 0.20
elif amount > 2000:
    discount = amount * 0.10
else:
    discount = 0
print("Discount =", discount)

# 30. Traffic Signal
signal = input("Enter signal (Red/Yellow/Green): ").lower()
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid Signal")