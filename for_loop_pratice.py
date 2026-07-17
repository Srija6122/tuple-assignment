# 1. Print numbers from 1 to 10, excluding 5

print("Numbers from 1 to 10 (excluding 5):")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# 2. Print each string in uppercase

def print_uppercase(words):
    print("\nStrings in Uppercase:")
    for word in words:
        print(word.upper())

words = ["python", "java", "html", "css"]
print_uppercase(words)


# 3. Sum of all even numbers in a list

numbers = [10, 15, 20, 25, 30, 35, 40]
even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num

print("\nSum of Even Numbers:", even_sum)


# 4. Iterate over a dictionary

student = {
    "Name": "Srija",
    "Age": 21,
    "Course": "Python"
}

print("\nDictionary Key-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)


# 5. First 10 Fibonacci numbers

print("\nFirst 10 Fibonacci Numbers:")
a, b = 0, 1

for i in range(10):
    print(a)
    a, b = b, a + b


# 6. Calculate average exam score

scores = [75, 82, 90, 68, 85]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print("\nAverage Score:", average)


# 7. Print a 5x5 matrix (1 to 25)

print("\n5x5 Matrix:")
num = 1

for i in range(5):
    for j in range(5):
        print(num, end="\t")
        num += 1
    print()