# 1. Sum of Squares

numbers = [1, 2, 3, 4, 5]
sum_of_squares = 0

for num in numbers:
    sum_of_squares += num ** 2

print("Sum of Squares:", sum_of_squares)


# 2. Print Each Character

def print_characters(text):
    for ch in text:
        print(ch)

word = input("Enter a string: ")
print_characters(word)


# 3. Find Maximum Number

numbers = [10, 45, 23, 89, 12, 67]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum Number:", maximum)


# 4. First 10 Fibonacci Numbers

a = 0
b = 1

print("First 10 Fibonacci Numbers:")

for i in range(10):
    print(a)
    a, b = b, a + b


# 5. Print Dictionary Key-Value Pairs

student = {
    "Name": "Srija",
    "Age": 21,
    "Course": "Python"
}

print("Dictionary Items:")

for key, value in student.items():
    print(key, ":", value)