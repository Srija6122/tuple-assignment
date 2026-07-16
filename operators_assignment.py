# 1. Rectangle Area and Perimeter
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print("Area =", area)
print("Perimeter =", perimeter)

# 2. Comparison Operators
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is smaller than", b)
else:
    print("Both numbers are equal")

# 3. Logical Operators
num = int(input("Enter a number: "))

if num >= 1 and num <= 100:
    print("Number is between 1 and 100")
else:
    print("Number is outside the range")

text = input("Enter a word: ")

if text == "python" or text == "Python":
    print("Matched")
else:
    print("Not matched")

# 4. Assignment and Augmented Assignment
x = 10
print("Initial x =", x)

x += 5
print("After += :", x)

x -= 2
print("After -= :", x)

x *= 3
print("After *= :", x)

x /= 2
print("After /= :", x)

x %= 4
print("After %= :", x)

x **= 2
print("After **= :", x)

# 5. Identity and Membership Operators
list1 = [10, 20, 30]
list2 = list1
list3 = [10, 20, 30]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)

print("20 in list1:", 20 in list1)
print("50 not in list1:", 50 not in list1)