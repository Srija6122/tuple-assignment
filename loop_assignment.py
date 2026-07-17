# 1. Countdown Timer
print("Countdown Timer:")
for i in range(10, 0, -1):
    print(i)
print("Boom!")

# 2. Lucky Numbers (Divisible by 7)
print("\nLucky Numbers:")
for i in range(1, 51):
    if i % 7 == 0:
        print(i, end=" ")
print()

# 3. Game Score Total
scores = [50, 65, 70]
total = 0
for score in scores:
    total += score
print("\nGame Score Total:", total)

# 4. Multiplication Table of 5
print("\nMultiplication Table of 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# 5. Count Vowels
text = input("\nEnter a string: ")
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print("Vowel Count:", count)

# 6. Swap Two Numbers
a = 10
b = 20
print("\nBefore Swap:", a, b)
a = a + b
b = a - b
a = a - b
print("After Swap:", a, b)

# 7. ATM Withdrawal
balance = 1000
withdrawals = [100, 200, 150]
for amount in withdrawals:
    balance -= amount
print("\nRemaining Balance:", balance)

# 8. Highest Marks
marks = [45, 78, 89, 66]
highest = marks[0]
for mark in marks:
    if mark > highest:
        highest = mark
print("Highest Marks:", highest)

# 9. Number Guess Check
guess = 25
for i in range(1, 51):
    if i == guess:
        print("Found Number:", i)
        break

# 10. Count Even Numbers
count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count += 1
print("Even Numbers Count:", count)

# 11. Reverse String
text = "python"
reverse = ""
for ch in text:
    reverse = ch + reverse
print("Reversed String:", reverse)

# 12. Shopping Cart Total
prices = [100, 250, 75]
total = 0
for price in prices:
    total += price
print("Shopping Cart Total:", total)

# 13. Rocket Launch Countdown
print("\nRocket Launch Countdown:")
for i in range(20, 0, -1):
    print(i)
print("Launch Successful!")

# 14. Count Uppercase Letters
text = "PyThOnPrOgRaM"
count = 0
for ch in text:
    if 'A' <= ch <= 'Z':
        count += 1
print("Uppercase Letters:", count)

# 15. String Length Without len()
text = "programming"
length = 0
for ch in text:
    length += 1
print("String Length:", length)

# 16. Palindrome Check
text = "madam"
reverse = ""
for ch in text:
    reverse = ch + reverse
if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# 17. Second Largest Number
numbers = [10, 45, 23, 89, 67]
largest = second = float('-inf')
for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second Largest:", second)

# 18. Simple Interest
principal = 1000
rate = 5
print("\nSimple Interest:")
for year in range(1, 6):
    interest = (principal * rate * year) / 100
    print(f"Year {year}: {interest}")

# 19. Sum of Odd Numbers
total = 0
for i in range(1, 51):
    if i % 2 != 0:
        total += i
print("Sum of Odd Numbers:", total)

# 20. Discount on Prices
prices = [500, 1000, 1500]
print("\nDiscounted Prices:")
for price in prices:
    print(price - price * 0.10)

# 21. Perfect Number
num = int(input("\nEnter a number to check Perfect Number: "))
sum_div = 0
for i in range(1, num):
    if num % i == 0:
        sum_div += i
if sum_div == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

# 22. Automorphic Number
num = int(input("Enter a number to check Automorphic: "))
square = num * num
if str(square).endswith(str(num)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")

# 23. Fibonacci Series
print("\nFibonacci Series:")
a, b = 0, 1
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()

# 24. Harshad Number
num = int(input("\nEnter a number to check Harshad Number: "))
digit_sum = 0
temp = num
while temp > 0:
    digit_sum += temp % 10
    temp //= 10

if num % digit_sum == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")