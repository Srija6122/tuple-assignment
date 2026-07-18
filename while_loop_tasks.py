# 1. Print numbers from 1 to 100

print("Numbers from 1 to 100:")
i = 1
while i <= 100:
    print(i, end=" ")
    i += 1

# 2. Fan Regulator (1 to 5 and back to 1)

print("\n\nFan Regulator:")
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1

i = 4
while i >= 1:
    print(i, end=" ")
    i -= 1

# 3. Print Even Numbers

print("\n\nEven Numbers (1-100):")
i = 2
while i <= 100:
    print(i, end=" ")
    i += 2

# 4. Print Odd Numbers

print("\n\nOdd Numbers (1-100):")
i = 1
while i <= 100:
    print(i, end=" ")
    i += 2

# 5. Sum of Numbers from 1 to n

n = int(input("\n\nEnter n: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print("Sum =", total)

# 6. Factorial

num = int(input("\nEnter a number for factorial: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print("Factorial =", fact)

# 7. Reverse a Number

num = int(input("\nEnter a number to reverse: "))
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
print("Reversed Number =", reverse)

# 8. Palindrome Check

num = int(input("\nEnter a number to check palindrome: "))
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# 9. Count Digits

num = int(input("\nEnter a number to count digits: "))
count = 0
temp = num
while temp > 0:
    count += 1
    temp //= 10
print("Number of Digits =", count)

# 10. Sum of Digits

num = int(input("\nEnter a number to find sum of digits: "))
digit_sum = 0
temp = num
while temp > 0:
    digit_sum += temp % 10
    temp //= 10
print("Sum of Digits =", digit_sum)