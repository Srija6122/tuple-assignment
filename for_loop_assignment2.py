# 1. Print each number and its square

numbers = [1, 2, 3, 4, 5]

print("Number and Square:")
for num in numbers:
    print(f"{num} -> {num ** 2}")


# 2. Print each character with its index

def print_characters_with_index(text):
    print("\nCharacters with Index:")
    for index, char in enumerate(text):
        print(f"Index {index}: {char}")

text = input("\nEnter a string: ")
print_characters_with_index(text)


# 3. Sum of even numbers in a list

numbers = [10, 15, 20, 25, 30, 35, 40]
even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num

print("\nSum of Even Numbers:", even_sum)


# 4. Print dictionary key-value pairs

student = {
    "Name": "Srija",
    "Age": 21,
    "Course": "Python"
}

print("\nDictionary Contents:")
for key, value in student.items():
    print(f"{key}: {value}")


# 5. Numbers from 1 to 100 divisible by 3 or 5

numbers = []

for i in range(1, 101):
    numbers.append(i)

print("\nNumbers divisible by 3 or 5:")
for num in numbers:
    if num % 3 == 0 or num % 5 == 0:
        print(num, end=" ")